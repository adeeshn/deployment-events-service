from fastapi import FastAPI, Response, status
from app.routers import deployments

app = FastAPI(title="Deployment Events App")

app.include_router(deployments.router)


@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=status.HTTP_204_NO_CONTENT)