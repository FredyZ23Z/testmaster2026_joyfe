from app import generar_token


def test_generar_token_devuelve_string_hexadecimal():
    token = generar_token()

    assert isinstance(token, str)
    assert len(token) == 32
    int(token, 16)


def test_generar_token_genera_valores_distintos():
    assert generar_token() != generar_token()
