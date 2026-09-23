def test_listar_productos_inicialmente_vacio(client, auth_headers):
    respuesta = client.get("/productos", headers=auth_headers)

    assert respuesta.status_code == 200
    assert respuesta.get_json() == []


def test_crud_completo_producto(client, auth_headers):
    nuevo = {"nombre": "Teclado", "precio": 19.99, "stock": 10}

    crear = client.post("/productos", json=nuevo, headers=auth_headers)
    assert crear.status_code == 201
    producto = crear.get_json()
    producto_id = producto["id"]
    assert producto["nombre"] == "Teclado"

    obtener = client.get(f"/productos/{producto_id}", headers=auth_headers)
    assert obtener.status_code == 200
    assert obtener.get_json()["precio"] == 19.99

    actualizado = {"nombre": "Teclado Pro", "precio": 29.99, "stock": 5}
    modificar = client.put(
        f"/productos/{producto_id}",
        json=actualizado,
        headers=auth_headers,
    )
    assert modificar.status_code == 200
    assert modificar.get_json()["nombre"] == "Teclado Pro"

    borrar = client.delete(f"/productos/{producto_id}", headers=auth_headers)
    assert borrar.status_code == 204

    inexistente = client.get(f"/productos/{producto_id}", headers=auth_headers)
    assert inexistente.status_code == 404


def test_crear_producto_con_datos_invalidos_devuelve_400(client, auth_headers):
    respuesta = client.post(
        "/productos",
        json={"nombre": "Teclado", "precio": -1, "stock": 10},
        headers=auth_headers,
    )

    assert respuesta.status_code == 400


def test_producto_inexistente_devuelve_404(client, auth_headers):
    assert client.get("/productos/999", headers=auth_headers).status_code == 404
    assert (
        client.put(
            "/productos/999",
            json={"nombre": "X", "precio": 1, "stock": 1},
            headers=auth_headers,
        ).status_code
        == 404
    )
    assert client.delete("/productos/999", headers=auth_headers).status_code == 404
