from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import FileResponse
from routers import posts, users, photos, auth

app = FastAPI()

# Add session support
SESSION_SECRET_KEY = "my_secret_key"
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET_KEY)

# Include routers
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(photos.router, prefix="/photos", tags=["photos"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

# Mount the directory for static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def main():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
