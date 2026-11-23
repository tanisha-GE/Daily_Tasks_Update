
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from dependencies.auth_dependencies import get_current_user
from database import get_db
from models.task import Task as TaskModel

import json
from redis_client import redis_client, clear_task_cache


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


@router.get("/")
def get_all_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    completed: Optional[bool] = None,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
     # 1. Create unique cache key
    cache_key = f"tasks:{current_user}:{skip}:{limit}:{completed}"

    # 2. Check Redis
    cached_tasks = redis_client.get(cache_key)

    if cached_tasks:
        print("Data coming from Redis")
        return json.loads(cached_tasks)

     # 3. Fetch data from SQLite
    print("Data coming from SQLite")
    query = db.query(TaskModel).filter(
        TaskModel.user == current_user
    )

    # Filtering
    if completed is not None:
        query = query.filter(
            TaskModel.completed == completed
        )
     # 5. Count total matching tasks
    total_tasks = query.count()

    # Pagination
    tasks = query.offset(skip).limit(limit).all()

    # Prepare response
    result = {
        "total_tasks": total_tasks,
        "skip": skip,
        "limit": limit,
        "tasks": [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
                "user": task.user
            }
            for task in tasks
        ]
    }

    # Save in Redis for 60 seconds
    redis_client.setex(
        cache_key,
        60,
        json.dumps(result)
    )

    print("Data saved in Redis")

    return result



@router.post("/", status_code=201)
def create_task(
    task: TaskCreate,
    db:Session=Depends(get_db),
    current_user: str = Depends(get_current_user)
):
   
    new_task = TaskModel(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user=current_user
    )


    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    clear_task_cache(current_user)

    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed,
            "user": new_task.user
        }
    }


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    existing_task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.user == current_user
    ).first()

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_task, key, value)

    db.commit()
    db.refresh(existing_task)
    clear_task_cache(current_user)

    return {
        "message": "Task updated successfully",
        "task": {
            "id": existing_task.id,
            "title": existing_task.title,
            "description": existing_task.description,
            "completed": existing_task.completed,
            "user": existing_task.user
        }
    }

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    # Find task belonging to the logged-in user
    existing_task = db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.user == current_user
    ).first()

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # Delete task from database
    db.delete(existing_task)
    db.commit()
    clear_task_cache(current_user)


    return {
        "message": "Task deleted successfully"
    }

