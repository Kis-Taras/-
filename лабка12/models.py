from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str

class User(BaseModel):
    name: str
    email: str
    password: str

class Photo(BaseModel):
    url: str
    description: str

class Token(BaseModel):
    access_token: str
    token_type: str
