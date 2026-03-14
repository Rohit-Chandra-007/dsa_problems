from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


@app.get("/")
def home():
    return {"message": "Hello from FastAPI 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("create")
def create(user: User):
    return user
