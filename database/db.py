import sqlite3


def init_db():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255),
            email VARCHAR(255)
            )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_servico VARCHAR(255),
            valor REAL
            )
    """)
    conn.commit()
    conn.close()


def create_cliente(nome, email):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cliente (nome, email) VALUES (?, ?)", (nome, email)
    )

    conn.commit()
    conn.close()


def create_servico(nome_servico, valor):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO servicos (nome_servico, valor) VALUES (?, ?)", (nome_servico, valor)
    )

    conn.commit()
    conn.close()


def get_cliente_nome(nome):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente WHERE nome = ?", (nome,))
    cliente = cursor.fetchall()
    conn.close
    return cliente


def get_servicos_nome(nome_servico):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicos WHERE nome = ?", (nome_servico,))
    servico = cursor.fetchall()
    conn.close
    return servico


def get_lista_cliente():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    cliente = cursor.fetchall()
    conn.close()

    return cliente


def get_lista_servicos():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicos")
    cliente = cursor.fetchall()
    conn.close()

    return cliente
