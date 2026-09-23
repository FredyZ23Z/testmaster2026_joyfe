def test_registro_crea_usuario(client, usuario):
    respuesta = client.post("/registro", json=usuario)

    assert respuesta.status_code == 201
    assert respuesta.get_json()["mensaje"] == "Usuario creado correctamente"


def test_registro_duplicado_devuelve_409(client, usuario):
    client.post("/registro", json=usuario)
    respuesta = client.post("/registro", json=usuario)

    assert respuesta.status_code == 409


def test_login_correcto_devuelve_token(client, usuario):
    client.post("/registro", json=usuario)

    respuesta = client.post("/login", json=usuario)

    assert respuesta.status_code == 200
    assert len(respuesta.get_json()["token"]) == 32


def test_login_incorrecto_devuelve_401(client, usuario):
    client.post("/registro", json=usuario)

    respuesta = client.post(
        "/login",
        json={"username": usuario["username"], "password": "incorrecta"},
    )

    assert respuesta.status_code == 401


def test_ruta_protegida_sin_token_devuelve_401(client):
    respuesta = client.get("/productos")

    assert respuesta.status_code == 401


def test_ruta_protegida_con_token_invalido_devuelve_401(client):
    respuesta = client.get(
        "/productos",
        headers={"Authorization": "Bearer token-invalido"},
    )

    assert respuesta.status_code == 401
