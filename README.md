# flyrank-crud-api

a small backend API to manage a simple to-do list. built with Python and FastAPI.
It supports all CRUD operations with a list of tasks saved in memory only.

## Installation
1. Install fastapi:
```
pip install fastapi "uvicorn[standard]"
```
2. run the local server:
```
uvicorn main:app --reload
```

## Api endpoints

- `GET /tasks`: view all the available tasks
- `GET /tasks/{task_id}`: view a specific task
- `POST /tasks`: add a new task
- `PUT /tasks/{task_id}`: change an existing task
- `DELETE /tasks/{task_id}`: remove a task

## Sample usage in Powershell
```
Invoke-RestMethod -Uri "http://localhost:8000/tasks" -Method Post -ContentType "application/json" -Body '{"title":"buy milk"}'

id title     done
-- -----     ----
 5 buy milk False
```

## Swagger UI screenshot:
![img.png](img.png)