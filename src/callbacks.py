import dearpygui.dearpygui as dpg
from src.utils import mostrar_mensagem
from database.db import *

# pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime


checkbox_tags_servicos = []  # salva os checkboxes
select_tags_clientes = []  # salva os checkboxes
servicos_cadastrados = get_lista_servicos()    # salva os serviços do banco


def cadastrar_dados_cliente():
    nome = dpg.get_value("campo_nome")
    email = dpg.get_value("campo_email")
    create_cliente(nome, email)
    # print(f"Nome: {nome}")
    # print(f"Email: {email}")
    mostrar_mensagem("mensagem_cliente", "✅ Cliente cadastrado com sucesso!", limpar_tags=[
                     "campo_nome", "campo_email"])


def cadastrar_dados_servico():
    servico = dpg.get_value("campo_servico")
    valor = dpg.get_value("campo_valor")
    create_servico(servico, valor)
    # print(f"Serviço: {servico}")
    # print(f"Valor: {valor}")
    mostrar_mensagem("mensagem_servico", "✅ Serviço cadastrado com sucesso!", limpar_tags=[
                     "campo_servico", "campo_valor"])


def gerar_servico():
    global servicos_cadastrados

    servicos_marcados = []
    for tag, servico in zip(checkbox_tags_servicos, servicos_cadastrados):
        if dpg.get_value(tag):
            servicos_marcados.append(servico)

    if not servicos_marcados:  # validação
        mostrar_mensagem("mensagem_pdf", "⚠️ Nenhum serviço selecionado!")
        return

    # ✅ pega o cliente selecionado
    cliente_selecionado = dpg.get_value("select_cliente")

    valor_total = sum(s[2]
                      for s in servicos_marcados)  # valor total dos serviços

    # print(f"👤 Cliente: {cliente_selecionado}")
    # print(f"\n💰 Valor total: R$ {valor_total:.2f}")

    mostrar_mensagem("mensagem_pdf", "📄 PDF gerado com sucesso!")

    # pegando os valores das variaveis
    criar_pdf(cliente_selecionado, servicos_marcados, valor_total)


# criando o pdf
def criar_pdf(cliente, servicos, valor_total):
    data_atual = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = f"orcamento_{cliente}_{data_atual}.pdf"

    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    # cabeçalho
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, altura - 20, f"Sistema de Emissão de Orçamentos")
    c.drawString(50, altura - 50, f"Orçamento para: {cliente}")

    c.setFont("Helvetica", 12)
    c.drawString(50, altura - 80,
                 f"Data: {datetime.datetime.now().strftime('%d/%m/%Y')}")

    # Tabela de serviços
    y = altura - 130
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Serviços:")
    y -= 20

    c.setFont("Helvetica", 12)
    for servico in servicos:
        nome = servico[1]
        valor = servico[2]
        c.drawString(60, y, f"- {nome} - R$ {valor:.2f}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Valor Total: R$ {valor_total:.2f}")

    c.save()
    print(f"📄 PDF salvo como: {nome_arquivo}")
