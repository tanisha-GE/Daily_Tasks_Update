Task Manager API

A simple Task Management REST API built using Python and FastAPI.

Features
Create a task
View all tasks
View task by ID
Update a task
Mark task as completed
Delete a task
Technologies Used
Python
FastAPI
Uvicorn
Pydantic
Installation
bash
pip install fastapi uvicorn

Run Application
bash
uvicorn main:app --reload

API Documentation

Open Swagger UI:

http://127.0.0.1:8000/docs

API Endpoints
Method	Endpoint	Description
POST	/tasks	Create task
GET	/tasks	Get all tasks
GET	/tasks/{task_id}	Get task by ID
PUT	/tasks/{task_id}	Update task
PATCH	/tasks/{task_id}/complete	Complete task
DELETE	/tasks/{task_id}	Delete task
Learning Objectives
Understand Client–Server Architecture
Learn HTTP Methods and Status Codes
Understand REST API Fundamentals
Practice CRUD Operations
Test APIs using Swagger UI

Note: Currently uses in-memory storage. Data is not persistent after restarting the application.