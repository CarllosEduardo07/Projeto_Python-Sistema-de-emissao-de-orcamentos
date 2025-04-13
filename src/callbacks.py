import dearpygui.dearpygui as dpg
from src.utils import mostrar_mensagem


servicos_cadastrados = [
    {"nome": "manutenção de computador", "valor": 100},
    {"nome": "manutenção de Notebook", "valor": 130},
    {"nome": "limpeza do computador", "valor": 70},
    {"nome": "troca do teclado do Notebook", "valor": 150},
    {"nome": "troca da bateria", "valor": 120},
]

checkbox_tags_servicos = []  # salva os serviços marcados


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

    servicos_marcados = []  # pegando os serviços marcados
    for tag, servico in zip(checkbox_tags_servicos, servicos_cadastrados):
        if dpg.get_value(tag):
            servicos_marcados.append(servico)

    if not servicos_marcados:  # validação
        mostrar_mensagem("mensagem_pdf", "⚠️ Nenhum serviço selecionado!")
        return

   # print
    for s in servicos_marcados:
        print(f"✅ {s['nome']} - R$ {s['valor']}")

    mostrar_mensagem("mensagem_pdf", "📄 PDF gerado com sucesso!")
