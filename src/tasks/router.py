from fastapi import APIRouter,Depends,status
from typing import List
from src.tasks import controller
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helpers import authenticate_user
task_routes = APIRouter(prefix="/tasks",tags=["Tasks"])
from src.tasks.dtos import TaskCreateDTO,TaskResponseDTO
from src.user.models import UserModel

@task_routes.post("/create",response_model=TaskResponseDTO,status_code=status.HTTP_201_CREATED)
def create_task(body: TaskCreateDTO,db=Depends(get_db),user: UserModel=Depends(authenticate_user)):
    return controller.create_task(body,db)

@task_routes.get("/get-all",response_model=List[TaskResponseDTO],status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session=Depends(get_db),user: UserModel=Depends(authenticate_user)):
    return controller.get_all_tasks(db)

@task_routes.get("/get_task/{task_id}",response_model=TaskResponseDTO,status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int,db:Session=Depends(get_db),user: UserModel=Depends(authenticate_user)):
    return controller.get_task_by_id(task_id,db)


@task_routes.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id:int,db:Session=Depends(get_db),user: UserModel=Depends(authenticate_user)):
    return controller.delete_task_by_id(task_id,db)

@task_routes.put("/update_task/{task_id}",response_model=TaskResponseDTO,status_code=status.HTTP_200_OK)
def update_task(task_id:int,body: TaskCreateDTO,db:Session=Depends(get_db),user: UserModel=Depends(authenticate_user)):
    return controller.update_task(task_id,body,db)