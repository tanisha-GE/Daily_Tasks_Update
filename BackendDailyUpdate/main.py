from fastapi import FastAPI
#import routes
from routers.auth_routes import router as auth_router
from routers.task_routes import router as task_router
#import for db conn
from database import engine,Base
from models import task, user
#CORS
from fastapi.middleware.cors import CORSMiddleware
#Exception
from exceptions import general_exception_handler
from middleware.logging_middleware import logging_middleware

app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)
app.middleware("http")(logging_middleware)
app.add_exception_handler(
    Exception,
    general_exception_handler
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
Base.metadata.create_all(bind=engine)

#include router
app.include_router(auth_router)
app.include_router(task_router)
