from fastapi import FastAPI
from pydantic.main import BaseModel

# Create the main FastAPI application instance.
# This is similar to the main entry point of your API app.
app = FastAPI()


class User(BaseModel):
    # Pydantic model used to validate incoming JSON data.
    # FastAPI checks that `name`, `age`, and `email` are provided with the correct types.
    name: str
    age: int
    email: str


@app.get("/")
def home():
    # Basic route for the home page.
    # Returns a JSON response.
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health():
    # Health check endpoint.
    # Commonly used to confirm that the API is running.
    return {"status": "ok"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    # `user_id` comes from the URL path.
    # FastAPI converts it to an integer automatically because of `: int`.
    return {"user_id": user_id}


@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    # This route shows how to read multiple path parameters from the URL.
    return {"user": user_id, "post": post_id}


@app.post("/create")
def create(user: User):
    # `user` is read from the request body as JSON.
    # FastAPI validates the body using the `User` model before this function runs.
    return user


@app.patch("/posts/{id}")
def update_post(id: int):
    return "hello world"
