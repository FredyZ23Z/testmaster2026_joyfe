import sqlite3

from app import init_db


TABLAS_ESPERADAS = {"usuarios", "tokens", "productos", "clientes"}


def test_init_db_crea_las_tablas(db_path):
    init_db(str(db_path))

    conexion = sqlite3.connect(db_path)
    try:
        filas = conexion.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
    finally:
        conexion.close()

    tablas = {fila[0] for fila in filas}
    assert TABLAS_ESPERADAS.issubset(tablas)


def test_init_db_es_idempotente(db_path):
    init_db(str(db_path))
    init_db(str(db_path))

    conexion = sqlite3.connect(db_path)
    try:
        resultado = conexion.execute("SELECT COUNT(*) FROM usuarios").fetchone()[0]
    finally:
        conexion.close()

    assert resultado == 0
