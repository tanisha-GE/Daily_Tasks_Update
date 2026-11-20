from fastapi import APIRouter

router=APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)
@router.get("/")
def get_all_tasks():
    return {"message":"all tasks"}

@router.post("/")
def create_task():
    return {"message:" "Task created"}