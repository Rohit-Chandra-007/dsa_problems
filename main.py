import uvicorn


def dev():
    uvicorn.run("app.app:app", reload=True)


def start():
    uvicorn.run("app.app:app")
