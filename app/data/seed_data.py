from datetime import datetime, timedelta, UTC


def seed_deployments():
    base_time = datetime(2025, 4, 28, 14, 0, tzinfo=UTC)

    services = [
        "billing-api",
        "auth-service",
        "orders-api",
        "notifications-service",
        "inventory-service",
    ]

    statuses = [
        "success",
        "failed",
        "success",
        "success",
        "failed",
        "success",
    ]

    deployments = []

    for i in range(30):
        service = services[i % len(services)]
        status = statuses[i % len(statuses)]

        deployments.append(
            {
                "id": f"deploy_{i + 1:03}",
                "service": service,
                "status": status,
                "duration": 120 + (i * 17) % 400,
                "timestamp": (
                    base_time + timedelta(hours=i * 3)
                ).isoformat(),
                "commit_sha": f"abc{i + 1000:04x}",
            }
        )

    return deployments