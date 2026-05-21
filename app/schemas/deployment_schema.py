from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class DeploymentStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"


class DeploymentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(..., examples=["deploy_123"])
    service: str = Field(..., examples=["billing-api"])
    status: DeploymentStatus = Field(..., examples=["failed"])
    duration: int = Field(..., ge=0, description="Deployment duration in seconds")
    timestamp: datetime = Field(..., examples=["2025-04-28T14:32:00Z"])
    commit_sha: str = Field(..., examples=["abc123"])


class DeploymentListResponse(BaseModel):
    deployments: list[DeploymentResponse]
    count: int