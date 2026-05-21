from app.data.seed_data import seed_deployments


class DeploymentRepository:
    def __init__(self):
        self.deployments = seed_deployments()

    def list(self):
        return self.deployments


deployment_repository = DeploymentRepository()