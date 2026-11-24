# FastAPI Task Manager API

A Task Management REST API built using **FastAPI, Python, SQLite, SQLAlchemy, and JWT Authentication**.

## Technologies Used

- FastAPI – Backend framework
- Python – Programming language
- SQLite – Database
- SQLAlchemy – ORM
- Pydantic – Data validation
- JWT – Authentication
- Argon2 – Password hashing
- Redis – Caching
- Postman / Swagger UI – API testing

## Features Implemented

- User registration and login
- Secure password hashing using Argon2
- JWT token generation and verification
- Authentication and user-based authorization
- SQLite database integration using SQLAlchemy
- Task CRUD operations (Create, Read, Update, Delete)
- Users can create and manage only their own tasks
- Database indexing for faster data retrieval
- Query optimization to improve database performance
- Pagination to retrieve tasks in smaller sets
- Filtering tasks based on completion status
- Redis caching to reduce repeated database queries
- Cache expiration using TTL (60 seconds)
- Cache invalidation after creating, updating, or deleting tasks

## API Endpoints

| Operation | Method | Endpoint |
|---|---|---|
| Register | POST | `/auth/register` |
| Login | POST | `/auth/login` |
| Create Task | POST | `/tasks/` |
| Get Tasks | GET | `/tasks/` |
| Update Task | PUT | `/tasks/{task_id}` |
| Delete Task | DELETE | `/tasks/{task_id}` |

### Pagination and Filtering Examples

```text
GET /tasks/?skip=0&limit=10
GET /tasks/?skip=10&limit=10
GET /tasks/?completed=true
GET /tasks/?completed=false
```

## Redis Caching

Redis is integrated to temporarily store task responses and reduce repeated database queries.

- First request fetches data from SQLite and stores it in Redis.
- Repeated requests with the same parameters retrieve data from Redis.
- Cached data expires automatically after 60 seconds.
- Cache is cleared when a task is created, updated, or deleted.

## Project Structure

```text
BackendDailyUpdate/
├── main.py
├── database.py
├── config.py
├── redis_client.py
├── requirements.txt
├── models/
│   ├── task.py
│   └── user.py
├── routers/
│   ├── auth_routes.py
│   └── task_routes.py
├── services/
│   ├── auth_services.py

├── dependencies/
│   └── auth_dependencies.py
└── middleware/
    └── logging_middleware.py
```

## Run the Project

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Redis
sudo systemctl start redis-server

# Start FastAPI server
uvicorn main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs

## Upcoming Improvements

- Background jobs using FastAPI BackgroundTasks

## Project StatusBackground jobs and async tasks

Core authentication, database operations, CRUD functionality, query optimization, pagination, filtering,Password hashing and authentication security and Redis caching have been implemented,.