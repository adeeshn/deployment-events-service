from fastapi import FastAPI
from app.routers import deployments


app = FastAPI(title="FastAPI App")

app.include_router(deployments.router)


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}"}