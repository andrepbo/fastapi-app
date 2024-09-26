from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for Task
class Task(BaseModel):
    id: int
    title: str
    description: str

# In-memory data store
tasks = [
    Task(id=1, title="Learn Flask", description="Understand how Flask works."),
    Task(id=2, title="Learn FastAPI", description="Get familiar with FastAPI.")
]

# Get all tasks
@app.get('/tasks', response_model=List[Task])
def get_tasks():
    return tasks

# Get task by ID
@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

# Create a new task
@app.post('/tasks', response_model=Task, status_code=201)
def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

# Update an existing task
@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    return task

# Delete a task
@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)