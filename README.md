# Deployment Events Service

A lightweight FastAPI backend service for ingesting and serving deployment event data.

---

# Features

- List deployment events
- Filter deployments by service and status
- Retrieve deployment details by ID
- Clean layered architecture:
  - Router layer
  - Service layer
  - Repository/storage abstraction
- In-memory seeded dataset
- Docker support

---

# Tech Stack

- Python 3.14
- FastAPI
- Poetry
- Docker

---

# Project Structure

```text
deployment-events/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── repositories/
│   ├── schemas/
│   ├── models/
│   ├── data/
│   └── utils/
│
├── tests/
├── README.md
├── pyproject.toml
├── poetry.lock
└── Dockerfile
```

---

# Local Setup

## 1. Install dependencies

```bash
poetry install
```

## 2. Start the server

```bash
poetry run uvicorn app.main:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```

---

# API Endpoints

## List deployments

```http
GET /deployments
```

Optional query parameters:

| Parameter | Description |
|---|---|
| `service` | Filter by service name |
| `status` | Filter by deployment status |

Examples:

```http
GET /deployments?service=billing-api
GET /deployments?status=failed
```

---

## Get deployment by ID

```http
GET /deployments/{deployment_id}
```

Example:

```http
GET /deployments/deploy_001
```

---

# OpenAPI Docs & Interactive Testing

FastAPI automatically generates interactive API documentation that can be used for testing:

- **Swagger UI (interactive testing):**
  ```text
  http://127.0.0.1:8000/docs
  ```
  This is a fully interactive interface where you can test all API endpoints directly. Click any endpoint to expand it, fill in parameters, and see live responses. Perfect for exploring the API without writing code.

- **ReDoc (Read-Only Documentation):**
  ```text
  http://127.0.0.1:8000/redoc
  ```
  Provides a clean, read-only view of the API schema.

---

# Running with Docker

## Build image

```bash
docker build --no-cache -t deployment-events-service .
```

## Run container

```bash
docker run -p 8000:8000 deployment-events-service
```

The application will be available at:

```text
http://localhost:8000
```

---

# Notes

- Storage is intentionally in-memory for simplicity and fast iteration.
- The repository layer abstracts storage concerns, allowing future migration to SQLite or Postgres without changing the API layer.
- The architecture is intentionally lightweight but designed to be easily extensible during live coding exercises.
- Docker support is included for reproducible local execution.