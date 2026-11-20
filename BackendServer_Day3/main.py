from fastapi import FastAPI
from routers.auth_routes import router as auth_router

app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)

app.include_router(auth_router)