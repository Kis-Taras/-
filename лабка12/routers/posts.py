from fastapi import APIRouter, HTTPException
from models import Post
from db import db, stats


router = APIRouter()

@router.get("/")
def read_posts():
    stats["GET /posts"] += 1
    return db

@router.post("/")
def create_post(post: Post):
    stats["POST /posts"] += 1
    post_id = f"post{len(db)+1}"
    db[post_id] = post.dict()
    return db[post_id]

@router.put("/{post_id}")
def update_post(post_id: str, post: Post):
    stats["PUT /posts"] += 1
    if post_id not in db:
        raise HTTPException(status_code=404, detail="Пост не знайдено")
    db[post_id] = post.dict()
    return db[post_id]

@router.delete("/{post_id}")
def delete_post(post_id: str):
    stats["DELETE /posts"] += 1
    if post_id not in db:
        raise HTTPException(status_code=404, detail="Пост не знайдено")
    del db[post_id]
    return {"message": "Пост видалено"}