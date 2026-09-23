def test_listar_clientes_inicialmente_vacio(client, auth_headers):
    respuesta = client.get("/clientes", headers=auth_headers)

    assert respuesta.status_code == 200
    assert respuesta.get_json() == []


def test_crud_completo_cliente(client, auth_headers):
    nuevo = {
        "nombre": "Ana",
        "email": "ana@example.com",
        "telefono": "600123123",
    }

    crear = client.post("/clientes", json=nuevo, headers=auth_headers)
    assert crear.status_code == 201
    cliente = crear.get_json()
    cliente_id = cliente["id"]
    assert cliente["email"] == "ana@example.com"

    obtener = client.get(f"/clientes/{cliente_id}", headers=auth_headers)
    assert obtener.status_code == 200

    actualizado = {
        "nombre": "Ana Gomez",
        "email": "ana.gomez@example.com",
        "telefono": "611222333",
    }
    modificar = client.put(
        f"/clientes/{cliente_id}",
        json=actualizado,
        headers=auth_headers,
    )
    assert modificar.status_code == 200
    assert modificar.get_json()["nombre"] == "Ana Gomez"

    borrar = client.delete(f"/clientes/{cliente_id}", headers=auth_headers)
    assert borrar.status_code == 204

    inexistente = client.get(f"/clientes/{cliente_id}", headers=auth_headers)
    assert inexistente.status_code == 404


def test_cliente_sin_telefono_guarda_cadena_vacia(client, auth_headers):
    respuesta = client.post(
        "/clientes",
        json={"nombre": "Luis", "email": "luis@example.com"},
        headers=auth_headers,
    )

    assert respuesta.status_code == 201
    assert respuesta.get_json()["telefono"] == ""


def test_crear_cliente_con_email_invalido_devuelve_400(client, auth_headers):
    respuesta = client.post(
        "/clientes",
        json={"nombre": "Ana", "email": "email-invalido"},
        headers=auth_headers,
    )

    assert respuesta.status_code == 400
