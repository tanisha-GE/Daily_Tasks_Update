from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from services.auth_services import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Temporary storage for learning.
# Later, we will use a database.
users = []


class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    username: str
    password: str


# Register API
@router.post("/register", status_code=201)
def register_user(user: UserRegister):

    # Check if username already exists
    for existing_user in users:
        if existing_user["username"] == user.username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

    hashed_password = hash_password(user.password)

    # Save user
    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "password": hashed_password
    }

    users.append(new_user)

    return {
        "message": "User registered successfully"
    }


# Login API
@router.post("/login")
def login_user(user: UserLogin):

    for existing_user in users:
        if existing_user["username"] == user.username:

            if verify_password(
                user.password,
                existing_user["password"]
            ):
                token = create_access_token(user.username)

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )
