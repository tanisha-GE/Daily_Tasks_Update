
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create FastAPI application
app = FastAPI(
    title="Task Manager API",
    description="A beginner-friendly Task Management REST API",
    version="1.0.0"
)

# Temporary in-memory storage
tasks = []

# Task request model
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


# 1. Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Task Manager API"}


# 2. Create a task
@app.post("/tasks", status_code=201)
def create_task(task: Task):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


# 3. Get all tasks
@app.get("/tasks")
def get_all_tasks():
    return {
        "total_tasks": len(tasks),
        "tasks": tasks
    }


# 4. Get task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# 5. Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed

            return {
                "message": "Task updated successfully",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# 6. Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# 7. Mark task as completed
@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:

            task["completed"] = True

            return {
                "message": "Task marked as completed",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
