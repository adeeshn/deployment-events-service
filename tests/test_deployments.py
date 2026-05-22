import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient

from app.main import app
import app.routers.deployments as deployments_module

client = TestClient(app)

class DummyService:
	def __init__(self):
		self._data = [
			{
				"id": "deploy_001",
				"service": "billing-api",
				"status": "success",
				"duration": 123,
				"timestamp": "2025-04-28T14:32:00Z",
				"commit_sha": "abc1001",
			},
			{
				"id": "deploy_002",
				"service": "auth-service",
				"status": "failed",
				"duration": 200,
				"timestamp": "2025-04-28T17:32:00Z",
				"commit_sha": "abc1002",
			},
			{
				"id": "deploy_003",
				"service": "billing-api",
				"status": "failed",
				"duration": 95,
				"timestamp": "2025-04-28T20:32:00Z",
				"commit_sha": "abc1003",
			},
		]

	def list_deployments(self, service: str | None = None, status: str | None = None):
		results = self._data
		if service:
			results = [d for d in results if d["service"] == service]
		if status:
			results = [d for d in results if d["status"] == status]
		return results

	def get_deployment(self, deployment_id: str):
		for d in self._data:
			if d["id"] == deployment_id:
				return d
		return None

def setup_dummy_service():
	deployments_module.deployment_service = DummyService()

def test_list_deployments_no_filters():
	setup_dummy_service()
	resp = client.get("/deployments")
	assert resp.status_code == 200
	body = resp.json()
	assert body["count"] == 3
	assert len(body["deployments"]) == 3

def test_list_deployments_filter_by_service():
	setup_dummy_service()
	resp = client.get("/deployments", params={"service": "billing-api"})
	assert resp.status_code == 200
	body = resp.json()
	assert body["count"] == 2
	assert all(d["service"] == "billing-api" for d in body["deployments"])

def test_list_deployments_filter_by_status():
	setup_dummy_service()
	resp = client.get("/deployments", params={"status": "failed"})
	assert resp.status_code == 200
	body = resp.json()
	assert body["count"] == 2
	assert all(d["status"] == "failed" for d in body["deployments"])

def test_get_deployment_found():
	setup_dummy_service()
	resp = client.get("/deployments/deploy_001")
	assert resp.status_code == 200
	body = resp.json()
	assert body["id"] == "deploy_001"
	assert body["service"] == "billing-api"

def test_get_deployment_not_found():
	setup_dummy_service()
	resp = client.get("/deployments/not-exist")
	assert resp.status_code == 404
	body = resp.json()
	assert "not found" in body["detail"].lower()
