# FastAPI Task Manager API

A Task Management REST API built using **FastAPI, Python, SQLite, SQLAlchemy, and JWT Authentication**.

## Technologies Used

- FastAPI – Backend framework
- SQLite – Database
- SQLAlchemy – ORM
- Pydantic – Data validation
- JWT – Authentication
- Argon2 – Password hashing
- Postman – API testing

## Features Implemented

- User registration and login
- Secure password hashing
- JWT token generation and verification
- Authentication and user-based authorization
- SQLite database integration using SQLAlchemy
- Task CRUD operations in database
- Users can create and manage only their own tasks

## API Endpoints

| Operation   | Method | Endpoint           |
| ----------- | ------ | ------------------ |
| Register    | POST   | `/auth/register`   |
| Login       | POST   | `/auth/login`      |
| Create Task | POST   | `/tasks/`          |
| Get Tasks   | GET    | `/tasks/`          |
| Update Task | PUT    | `/tasks/{task_id}` |
| Delete Task | DELETE | `/tasks/{task_id}` |

## Project Structure

```text
BackendDailyUpdate/
├── main.py
├── database.py
├── config.py
├── requirements.txt
├── models/
│   ├── task.py
│   └── user.py
├── routers/
│   ├── auth_routes.py
│   └── task_routes.py
├── services/
│   └── auth_services.py
└── dependencies/
    └── auth_dependencies.py
```

## Run the Project

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload
```

Open Swagger UI: [http://127.0.0.1:8000/docs]

## Upcoming Improvements

- Database indexing and query optimization
- Pagination and filtering
- Redis caching
- Background jobs and async tasks
