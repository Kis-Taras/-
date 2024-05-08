from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from routers import posts, users, photos, auth
from routers.posts import router as posts_router
from routers.users import router as users_router
from routers.auth import router as auth_router

app = FastAPI()

# Підключення роутерів
app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(photos.router, prefix="/photos", tags=["photos"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

# Підключення каталогу статичних файлів
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def main():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

