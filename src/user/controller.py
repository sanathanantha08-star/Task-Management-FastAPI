from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Request,status
import src.utils.db as db
from src.user.models import UserModel
from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta
from src.utils.settings import settings

from src.user.dtos import UserLoginSchema

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register(body: UserSchema, db: Session):
    print(body)
    #username validation
   
    is_user=db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code=400,detail="Username already exists")
    #email validation
    is_email=db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(status_code=400,detail="Email already exists")
    
    hash_password = get_password_hash(body.password)
    new_user=UserModel(
        name=body.name,
        username=body.username,
        email=body.email,
        hash_password=hash_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    if not new_user:
        raise HTTPException(status_code=500,detail="User registration failed")
    return new_user
    
    
def login_user(body: UserLoginSchema,db: Session):
    #check if user exists
    is_user_exists=db.query(UserModel).filter(UserModel.username == body.username).first()
    if not is_user_exists:
        raise HTTPException(status_code=401,detail="Invalid username")
    #check if password is correct
    if is_user_exists and not verify_password(body.password, is_user_exists.hash_password):
        raise HTTPException(status_code=401,detail="Invalid password")
    
    token=jwt.encode({
        "_id": is_user_exists.id,
        "username": is_user_exists.username,
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    },settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}



#AUTH TOKEN PASSED IN HEADERS
def authenticate_user(request: Request,db: Session):
    token=request.headers.get("Authorization")
    token=token.split(" ")[1] if token else None
    data=jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    user_id=data.get("_id")
    exp_time=data.get("exp")
    current_time=datetime.utcnow().timestamp()
    if current_time > exp_time:
        raise HTTPException(status_code=401,detail="Token expired")
    user=db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401,detail="Invalid token")
    return user
    

    
