from app.repositories.deployment_repository import deployment_repository


class DeploymentService:
    def __init__(self, repository):
        self.repository = repository

    def list_deployments(
        self,
        service: str | None = None,
        status: str | None = None,
    ):
        return self.repository.list(
            service=service,
            status=status,
        )

    def get_deployment(self, deployment_id: str):
        return self.repository.get_by_id(deployment_id)


deployment_service = DeploymentService(deployment_repository)
