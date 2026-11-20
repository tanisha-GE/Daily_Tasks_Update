
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from dependencies.auth_dependencies import get_current_user
from database import get_db
from models.task import Task as TaskModel

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
    db: Session=Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    tasks=db.query(TaskModel).filter(
        TaskModel.user== current_user
    ).all()
    return {
        "total_tasks": len(tasks),
        "tasks": tasks
    }


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
