from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.deployment_schema import (
    DeploymentListResponse,
    DeploymentResponse,
    DeploymentStatus,
)
from app.services.deployment_service import deployment_service

router = APIRouter(prefix="/deployments", tags=["deployments"])


@router.get("", response_model=DeploymentListResponse)
def list_deployments(
    service: str | None = Query(default=None, description="Filter by service name"),
    status_filter: DeploymentStatus | None = Query(
        default=None,
        alias="status",
        description="Filter by deployment status",
    ),
) -> DeploymentListResponse:
    deployments = deployment_service.list_deployments(
        service=service,
        status=status_filter.value if status_filter else None,
    )

    return DeploymentListResponse(
        deployments=deployments,
        count=len(deployments),
    )


@router.get("/{deployment_id}", response_model=DeploymentResponse)
def get_deployment(deployment_id: str) -> DeploymentResponse:
    deployment = deployment_service.get_deployment(deployment_id)

    if deployment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deployment '{deployment_id}' not found",
        )

    return deployment
