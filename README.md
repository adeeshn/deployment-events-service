# deployment-events

A small FastAPI-style service for deployment event tracking and metrics.

## Project structure

```text
deployment-events/
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── deployments.py
│   ├── services/
│   │   ├── deployment_service.py
│   │   └── metrics_service.py
│   ├── repositories/
│   │   └── deployment_repository.py
│   ├── models/
│   │   └── deployment.py
│   ├── schemas/
│   │   ├── deployment_schema.py
│   │   ├── metrics_schema.py
│   │   └── compare_schema.py
│   ├── data/
│   │   └── seed_data.py
│   └── utils/
│       └── metrics.py
│
├── tests/
│   └── test_deployments.py
├── README.md
├── pyproject.toml
├── poetry.lock
├── Dockerfile
└── .gitignore
```

## Notes

- `app/main.py`: application entrypoint
- `app/routers/deployments.py`: API router for deployment endpoints
- `app/services/`: business logic and metrics computation
- `app/repositories/deployment_repository.py`: persistence layer
- `app/models/deployment.py`: deployment domain model
- `app/schemas/`: request/response schemas
- `app/data/seed_data.py`: example/development seed data
- `app/utils/metrics.py`: helper utilities for metrics
- `tests/test_deployments.py`: deployment-related tests

## Usage

Update this section with the commands you use to run, test, and containerize the service.
