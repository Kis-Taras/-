from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from models import Token
from fastapi.responses import RedirectResponse

router = APIRouter()

SECRET_KEY = "1111"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_password_hash(password):
    return pwd_context.hash(password)

fake_users_db = {
    "Taras": {
        "username": "Taras",
        "password": "12345",
        "full_name": "Taras Kis",
        "email": "taraskis06@gmail.com",
        "hashed_password": get_password_hash("12345"),
        "disabled": False,
    }
}

def authenticate_user(fake_db, username: str, password: str):
    user = fake_db.get(username)
    if not user:
        return False
    if not pwd_context.verify(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token")
def login_for_access_token(response: Response, request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )

    # Set session data
    request.session['username'] = user['username']
    request.session['access_token'] = access_token

    expires = datetime.utcnow() + access_token_expires
    expires_timestamp = int(expires.timestamp())
    response.set_cookie(
        key="access_token",
        value=access_token,
        expires=expires_timestamp,
        httponly=True,
        secure=True,  # Set secure parameter to True
        samesite="Lax",
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile")
async def user_profile(token: str = Depends(oauth2_scheme)):
    user = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return {"message": f"Привіт! Це ваш профіль, {user['sub']}."}

