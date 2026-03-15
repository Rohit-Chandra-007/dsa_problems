import uvicorn


def dev():
    # Start the FastAPI app in development mode.
    # `reload=True` watches for file changes and restarts the server automatically.
    uvicorn.run("app.app:app", reload=True)


def start():
    # Start the FastAPI app in normal mode.
    # This runs the same app without auto-reload, which is closer to production usage.
    uvicorn.run("app.app:app")
