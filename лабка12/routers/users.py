from fastapi import APIRouter, HTTPException
from models import User
from db import users_db, stats

router = APIRouter()

@router.get("/")
def read_users():
    stats["GET /users"] += 1
    return users_db

@router.post("/{user_id}")
def create_user(user_id: str, user: User):
    stats["POST /users"] += 1
    if user_id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user_id] = user.dict()
    return users_db[user_id]

