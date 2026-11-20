from fastapi import FastAPI
#import routes
from routers.auth_routes import router as auth_router
from routers.task_routes import router as task_router
#import for db conn
from database import engine,Base
from models import task, user


app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

#include router
app.include_router(auth_router)
app.include_router(task_router)
