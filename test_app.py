import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_all_tasks():
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_task_by_id():
    response = client.get('/tasks/1')
    assert response.status_code == 200
    assert response.json()["title"] == "Learn Flask"

def test_create_task():
    new_task = {"id": 3, "title": "New Task", "description": "Task for testing"}
    response = client.post('/tasks', json=new_task)
    assert response.status_code == 201
    assert response.json()["title"] == "New Task"

def test_update_task():
    updated_task = {"id": 1, "title": "Updated Task", "description": "Updated description"}
    response = client.put('/tasks/1', json=updated_task)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

def test_delete_task():
    response = client.delete('/tasks/1')
    assert response.status_code == 204
    # Ensure task is deleted
    response = client.get('/tasks/1')
    assert response.status_code == 404