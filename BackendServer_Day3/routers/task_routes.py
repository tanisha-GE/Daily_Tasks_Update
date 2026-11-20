
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional

from dependencies.auth_dependencies import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

tasks = []


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


@router.get("/")
def get_all_tasks(
    current_user: str = Depends(get_current_user)
):
    return {
        "total_tasks": len(tasks),
        "tasks": tasks
    }


@router.post("/", status_code=201)
def create_task(
    task: Task,
    current_user: str = Depends(get_current_user)
):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "user": current_user
    }

    tasks.append(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }
