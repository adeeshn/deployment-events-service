from fastapi import APIRouter

router = APIRouter(prefix="/deployments", tags=["deployments"])

@router.get("/")
def get_deployments():
    return {"message": "List of deployments"}