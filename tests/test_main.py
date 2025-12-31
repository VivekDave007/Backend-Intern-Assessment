import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import User, Base
from app.database import engine
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))

@pytest.fixture(scope="function")
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_register_user(client, db):
    user_data = {
        "email": "testuser@example.com",
        "full_name": "Test User",
        "password": "password123"
    }
    response = client.post("/api/auth/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["email"] == user_data["email"]

def test_register_duplicate_email(client, db):
    user_data = {
        "email": "duplicate@example.com",
        "full_name": "Test User",
        "password": "password123"
    }
    client.post("/api/auth/register", json=user_data)
    response = client.post("/api/auth/register", json=user_data)
    assert response.status_code == 400

def test_login_user(client, db):
    user_data = {
        "email": "login@example.com",
        "full_name": "Login Test",
        "password": "password123"
    }
    client.post("/api/auth/register", json=user_data)
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    response = client.post("/api/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
