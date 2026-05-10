

from fastapi import HTTPException

from src.tasks.dtos import TaskCreateDTO
from src.utils.db import get_db
from sqlalchemy.orm import Session


from src.tasks.models import TaskModel
from src.utils import db
def create_task(body: TaskCreateDTO,db: db.LocalSession):
    data=body.model_dump()
    newTask = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
        )
    db.add(newTask)
    db.commit()
    db.refresh(newTask)
    return newTask


def get_all_tasks(db: db.LocalSession):
    tasks=db.query(TaskModel).all()
    return tasks

def get_task_by_id(id:int,db: db.LocalSession):
    task=db.query(TaskModel).filter(TaskModel.id==id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task


def delete_task_by_id(id:int,db: db.LocalSession):
    task=db.query(TaskModel).filter(TaskModel.id==id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(task)
    db.commit()
    return None

def update_task(id:int,body: TaskCreateDTO,db: db.LocalSession):
    task=db.query(TaskModel).filter(TaskModel.id==id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")

    task.title=body.title
    task.description=body.description
    task.is_completed=body.is_completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task