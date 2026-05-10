from fastapi import FastAPI
from src.utils.db import get_db, Base, engine
from src.tasks.router import task_routes
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(task_routes)