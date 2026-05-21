from app.data.seed_data import seed_deployments


class DeploymentRepository:
    def __init__(self):
        self.deployments = seed_deployments()

    def list(
        self,
        service: str | None = None,
        status: str | None = None,
    ):
        results = self.deployments

        if service:
            results = [
                deployment
                for deployment in results
                if deployment["service"] == service
            ]

        if status:
            results = [
                deployment
                for deployment in results
                if deployment["status"] == status
            ]

        return results

    def get_by_id(self, deployment_id: str):
        for deployment in self.deployments:
            if deployment["id"] == deployment_id:
                return deployment
        return None


deployment_repository = DeploymentRepository()