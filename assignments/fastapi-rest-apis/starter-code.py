from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="API de Tarefas")

tasks = {
    1: {"id": 1, "title": "Estudar FastAPI", "completed": False},
    2: {"id": 2, "title": "Criar uma rota", "completed": True},
}


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
