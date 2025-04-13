import dearpygui.dearpygui as dpg
from src.utils import mostrar_mensagem
from database.db import *


checkbox_tags_servicos = []  # salva os checkboxes
servicos_cadastrados = get_lista_servicos()    # salva os serviços do banco


def cadastrar_dados_cliente():
    nome = dpg.get_value("campo_nome")
    email = dpg.get_value("campo_email")
    create_cliente(nome, email)
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    mostrar_mensagem("mensagem_cliente", "✅ Cliente cadastrado com sucesso!", limpar_tags=[
                     "campo_nome", "campo_email"])


def cadastrar_dados_servico():
    servico = dpg.get_value("campo_servico")
    valor = dpg.get_value("campo_valor")
    create_servico(servico, valor)
    print(f"Serviço: {servico}")
    print(f"Valor: {valor}")
    mostrar_mensagem("mensagem_servico", "✅ Serviço cadastrado com sucesso!", limpar_tags=[
                     "campo_servico", "campo_valor"])


def gerar_pdf():
    global servicos_cadastrados

    servicos_marcados = []
    for tag, servico in zip(checkbox_tags_servicos, servicos_cadastrados):
        if dpg.get_value(tag):
            servicos_marcados.append(servico)

    if not servicos_marcados:
        mostrar_mensagem("mensagem_pdf", "⚠️ Nenhum serviço selecionado!")
        return

    valor_total = sum(s[2] for s in servicos_marcados)

    print(f"\n💰 Valor total: R$ {valor_total:.2f}")

    mostrar_mensagem("mensagem_pdf", "📄 PDF gerado com sucesso!")
