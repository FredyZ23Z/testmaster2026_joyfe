from app import validar_cliente, validar_producto, validar_registro


def test_validar_registro_correcto():
    assert validar_registro({"username": "ana", "password": "1234"}) is None


def test_validar_registro_rechaza_cuerpo_invalido():
    assert validar_registro(None) == "Cuerpo de la peticion invalido"


def test_validar_registro_requiere_username():
    assert validar_registro({"password": "1234"}) == "El campo username es obligatorio"


def test_validar_registro_requiere_password_de_4_caracteres():
    assert (
        validar_registro({"username": "ana", "password": "123"})
        == "El campo password debe tener al menos 4 caracteres"
    )


def test_validar_producto_correcto():
    assert validar_producto({"nombre": "Teclado", "precio": 19.99, "stock": 10}) is None


def test_validar_producto_rechaza_precio_negativo():
    assert (
        validar_producto({"nombre": "Teclado", "precio": -1, "stock": 10})
        == "El campo precio debe ser un numero >= 0"
    )


def test_validar_producto_rechaza_stock_negativo():
    assert (
        validar_producto({"nombre": "Teclado", "precio": 10, "stock": -1})
        == "El campo stock debe ser un entero >= 0"
    )


def test_validar_producto_rechaza_stock_decimal():
    assert (
        validar_producto({"nombre": "Teclado", "precio": 10, "stock": 1.5})
        == "El campo stock debe ser un entero >= 0"
    )


def test_validar_cliente_correcto():
    assert validar_cliente({"nombre": "Ana", "email": "ana@example.com"}) is None


def test_validar_cliente_rechaza_email_invalido():
    assert (
        validar_cliente({"nombre": "Ana", "email": "correo-invalido"})
        == "El campo email no es valido"
    )
