from types import new_class

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = [
    {"id": 1, "title": "buy groceries", "done": False},
    {"id": 2, "title": "read a book", "done": True},
    {"id": 3, "title": "write some code", "done": False},
    {"id": 4, "title": "check out on my friend", "done": True}
]

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"the task {task_id} is not found"})

@app.post("/tasks", status_code=201)
def create_task(task_data: dict):
    # when receiving a new task, we just need a title. the id will be auto generated, and the done will be false by default
    # first we need to confirm if we received a title and is not empty string
    if "title" not in task_data or not str(task_data["title"]).strip():
        return JSONResponse(status_code=400, content={"error": "the title is missing or empty"})
    # to generate an id, we need to see the largest id number available and add to it 1. if we dont have any tasks yet, we assign the default value 1 for the first task
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": task_data["title"],
        "done": False
    }
    tasks.append(new_task)
    return new_task

