from fastapi import APIRouter, HTTPException, Depends, status
from models import User
from db import users_db, stats
from routers.auth import oauth2_scheme

router = APIRouter()

@router.get("/")
def read_users():
    stats["GET /users"] += 1
    return users_db

@router.post("/")
def create_user(user: User):
    stats["POST /users"] += 1
    user_id = user.email  # Assuming email can be used as user_id, adjust accordingly
    if user_id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user_id] = user.dict()
    return users_db[user_id]

@router.get("/profile")
async def user_profile(token: str = Depends(oauth2_scheme)):
    return {"message": "Привіт! Це ваш профіль."}
