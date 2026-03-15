import uvicorn
from fastapi import FastAPI
from app.api.routes import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)

def dev():
    """Start the FastAPI app in development mode."""
    uvicorn.run("app.main:app", reload=True)

def start():
    """Start the FastAPI app in normal mode."""
    uvicorn.run("app.main:app")
