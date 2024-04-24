from fastapi import APIRouter
from models import Photo
from db import photos_db, stats



router = APIRouter()

@router.get("/")
def read_photos():
    stats["GET /photos"] += 1
    return photos_db