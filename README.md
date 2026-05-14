# FastAPI Task Management API

A basic Task Management REST API built using FastAPI, SQLAlchemy, and Pydantic with JWT Authentication.

## Features

* User Registration
* User Login Authentication
* JWT Token Based Authentication
* Create Tasks
* Get All Tasks
* Get Task By ID
* Update Tasks
* Delete Tasks
* PostgreSQL Database Integration
* Alembic Database Migrations
* Request Validation using Pydantic
* Layered Architecture using Controllers, DTOs, Models, and Routers

---

# Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Alembic
* JWT Authentication
* Uvicorn

---

# Project Structure

```bash
Task-Management/
│
├── src/
│   ├── tasks/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── utils/
│   │   ├── db.py
│   │   ├── helpers.py
│   │   ├── settings.py
│   │   └── constant.py
│   │
│   └── __init__.py
│
├── migrations/
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd Task-Management
```

---

## Create Virtual Environment

```bash
python3 -m venv env
```

Activate environment:

### Mac/Linux

```bash
source env/bin/activate
```

### Windows

```bash
env\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in root directory.

```env
DB_CONNECTION=postgresql://username:password@localhost:5432/taskdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Run Database Migrations

## Create Migration

```bash
alembic revision --autogenerate -m "initial migration"
```

## Apply Migration

```bash
alembic upgrade head
```

---

# Run Application

```bash
python3 -m uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

Redoc Docs:

```bash
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

# User Routes

## Register User

```http
POST /user/register
```

## Login User

```http
POST /user/login
```

## Authenticate User

```http
GET /user/authenticate
```

---

# Task Routes

## Create Task

```http
POST /tasks/create
```

## Get All Tasks

```http
GET /tasks/get-all
```

## Get Task By ID

```http
GET /tasks/get_task/{task_id}
```

## Update Task

```http
PUT /tasks/update_task/{task_id}
```

## Delete Task

```http
DELETE /tasks/delete_task/{task_id}
```

---

# Authentication

Protected routes require JWT Token.

Example:

```http
Authorization: Bearer <your_token>
```

---

# Dependencies

```txt
FastAPI
SQLAlchemy
Pydantic
Alembic
PostgreSQL
Uvicorn
```

---

# Future Improvements

* Role Based Access Control
* Pagination
* Task Status Management
* Docker Support
* Unit Testing
* Redis Caching
* Background Jobs
* CI/CD Pipeline

---

# Author

Sanath Anantha
