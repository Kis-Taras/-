from fastapi import FastAPI
from routers import  photos
from db import stats
from routers.posts import router as posts_router
from routers.users import router as users_router

app = FastAPI()
app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(photos.router, prefix="/photos", tags=["photos"])
app.include_router(photos.router, prefix="/photos", tags=["photos"])

@app.get("/version")
def read_version():
    stats["GET /version"] += 1
    return {"version": "1.0.0"}

@app.get("/stats")
def get_stats():
    stats["GET /stats"] += 1
    return dict(stats)
