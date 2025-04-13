import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Sistema de Orçamentos', width=1000, height=650)

# === CONFIGURAÇÕES GERAIS ===

FRAME_RATE = 60  # frames por segundo
DELAY_SEGUNDOS = 5
DELAY_FRAMES = DELAY_SEGUNDOS * FRAME_RATE


# === FUNÇÃO AUXILIAR ===

def mostrar_mensagem(tag_msg, texto, limpar_tags=None):
    dpg.set_value(tag_msg, texto)
    dpg.configure_item(tag_msg, show=True)

    def ocultar():
        dpg.configure_item(tag_msg, show=False)
        if limpar_tags:
            for campo in limpar_tags:
                dpg.set_value(campo, "")

    dpg.set_frame_callback(dpg.get_frame_count() + DELAY_FRAMES, ocultar)


# === FUNÇÕES DE CALLBACK ===

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


def gerarPDF():
    servico = dpg.get_value("nome_do_servico")
    print(f"Gerando PDF do serviço: {servico}")

    mostrar_mensagem("mensagem_pdf", "📄 PDF gerado com sucesso!")


# === INTERFACE GRÁFICA ===

# JANELA 1 - CLIENTE
with dpg.window(label="Cadastro de Clientes", width=480, height=300, pos=(10, 10)):
    dpg.add_input_text(label="Nome", tag="campo_nome")
    dpg.add_input_text(label="Email", tag="campo_email")
    dpg.add_button(label="Cadastrar Cliente", callback=cadastrar_dados_cliente)
    dpg.add_text("", tag="mensagem_cliente", show=False, color=[0, 200, 0])

# JANELA 2 - SERVIÇOS
with dpg.window(label="Cadastro de Serviços", width=480, height=300, pos=(500, 10)):
    dpg.add_input_text(label="Nome do Serviço", tag="campo_servico")
    dpg.add_input_text(label="Valor", tag="campo_valor")
    dpg.add_button(label="Cadastrar Serviço", callback=cadastrar_dados_servico)
    dpg.add_text("", tag="mensagem_servico", show=False, color=[0, 200, 0])

# JANELA 3 - PDF e Seleção
with dpg.window(label="Geração de PDF", width=970, height=300, pos=(0, 310)):
    dpg.add_combo(
        label="Menu de Seleção",
        items=["Opção 1", "Opção 2", "Opção 3"],
        default_value="Opção 1"
    )
    dpg.add_checkbox(label="Escolher Serviço", tag="nome_do_servico")
    dpg.add_button(label="Gerar PDF", callback=gerarPDF)
    dpg.add_text("", tag="mensagem_pdf", show=False, color=[0, 200, 0])


# === EXECUÇÃO ===

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
