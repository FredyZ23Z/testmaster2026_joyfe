import sys
from pathlib import Path

import pytest

# Asegura que la raiz del proyecto este disponible para importar app.py
RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
if str(RAIZ_PROYECTO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROYECTO))

from app import crear_app


@pytest.fixture
def db_path(tmp_path):
    return tmp_path / "test.db"


@pytest.fixture
def app(db_path):
    app = crear_app(str(db_path))
    app.config.update(TESTING=True)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def usuario():
    return {"username": "ana", "password": "1234"}


@pytest.fixture
def token(client, usuario):
    respuesta = client.post("/registro", json=usuario)
    assert respuesta.status_code == 201

    respuesta = client.post("/login", json=usuario)
    assert respuesta.status_code == 200

    return respuesta.get_json()["token"]


@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
