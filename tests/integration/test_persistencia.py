import sqlite3


def test_producto_se_guarda_realmente_en_sqlite(client, auth_headers, db_path):
    respuesta = client.post(
        "/productos",
        json={"nombre": "Monitor", "precio": 199.99, "stock": 3},
        headers=auth_headers,
    )
    assert respuesta.status_code == 201
    producto_id = respuesta.get_json()["id"]

    conexion = sqlite3.connect(db_path)
    try:
        fila = conexion.execute(
            "SELECT nombre, precio, stock FROM productos WHERE id = ?",
            (producto_id,),
        ).fetchone()
    finally:
        conexion.close()

    assert fila == ("Monitor", 199.99, 3)


def test_cliente_se_guarda_realmente_en_sqlite(client, auth_headers, db_path):
    respuesta = client.post(
        "/clientes",
        json={
            "nombre": "Carlos",
            "email": "carlos@example.com",
            "telefono": "600000000",
        },
        headers=auth_headers,
    )
    assert respuesta.status_code == 201
    cliente_id = respuesta.get_json()["id"]

    conexion = sqlite3.connect(db_path)
    try:
        fila = conexion.execute(
            "SELECT nombre, email, telefono FROM clientes WHERE id = ?",
            (cliente_id,),
        ).fetchone()
    finally:
        conexion.close()

    assert fila == ("Carlos", "carlos@example.com", "600000000")
