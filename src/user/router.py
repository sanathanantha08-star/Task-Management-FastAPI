from fastapi import APIRouter,Depends, status, Request
from sqlalchemy.orm import Session
from src.user import controller
from src.user.dtos import UserResponseSchema
from src.user.dtos import UserLoginSchema
user_routes = APIRouter(prefix="/user",tags=["Users"])
from src.user.dtos import UserSchema
from src.utils.db import get_db
from src.user.controller import authenticate_user

@user_routes.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)


@user_routes.post("/login",status_code=status.HTTP_200_OK)
def login_user(body:UserLoginSchema,db: Session = Depends(get_db)):
    return controller.login_user(body, db)

@user_routes.get("/authenticate",response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
def authenticate_user(request: Request,db: Session = Depends(get_db)):
    return controller.authenticate_user(request, db)
   