from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
  return {"status": "active", "message": "The Cloud Server is running 24/7!"}


class Task(BaseModel):
  topic: str


@app.post("/run-task")
def run_task(data: Task):
  return {
      "status": "success",
      "message": f"Task received for: {data.topic}",
  }
