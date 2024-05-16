from fastapi import APIRouter, HTTPException, status
from typing import List

from schemas.users import User, UserCreate
from db import db

router = APIRouter()
router.redirect_slashes = False

@router.get("/")
async def get_all_users() -> list[User]:
    """Получить список всех пользователей."""
    return list(db.users.values())

@router.get("/{id}")
async def get_user(id: int) -> User:
    """Получить информацию о конкретном пользователе."""
    user = db.users.get(id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate) -> User:
    """Создать нового пользователя."""
    new_id = max(db.users.keys() or (0,)) + 1
    user = User(id=new_id, **user_create.dict())
    db.users[new_id] = user
    return user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int) -> None:
    """Удалить существующего пользователя."""
    if id not in db.users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.users.pop(id)

@router.post("/{id}/comments", status_code=status.HTTP_201_CREATED)
async def add_comment(id: int, comment: str) -> User:
    """Добавить комментарий к пользователю."""
    user = db.users.get(id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user.comments.append(comment)
    return user
