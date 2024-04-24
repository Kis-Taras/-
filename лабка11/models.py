from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str

class User(BaseModel):
    name: str
    email: str

class Photo(BaseModel):
    url: str
    description: str