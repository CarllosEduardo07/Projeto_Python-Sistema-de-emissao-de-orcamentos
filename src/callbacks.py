import dearpygui.dearpygui as dpg
from src.utils import mostrar_mensagem


def cadastrar_dados_cliente():
    nome = dpg.get_value("campo_nome")
    email = dpg.get_value("campo_email")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    mostrar_mensagem("mensagem_cliente", "✅ Cliente cadastrado com sucesso!", limpar_tags=[
                     "campo_nome", "campo_email"])


def cadastrar_dados_servico():
    servico = dpg.get_value("campo_servico")
    valor = dpg.get_value("campo_valor")
    print(f"Serviço: {servico}")
    print(f"Valor: {valor}")
    mostrar_mensagem("mensagem_servico", "✅ Serviço cadastrado com sucesso!", limpar_tags=[
                     "campo_servico", "campo_valor"])


def gerar_pdf():
    servico = dpg.get_value("nome_do_servico")
    print(f"Gerando PDF do serviço: {servico}")
    mostrar_mensagem("mensagem_pdf", "📄 PDF gerado com sucesso!")
