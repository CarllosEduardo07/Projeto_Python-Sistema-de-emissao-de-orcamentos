import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='janela', width=1000, height=650)


def enviar_dados_cliente():
    nome = dpg.get_value("campo_nome")
    email = dpg.get_value("campo_email")

    print(f"Nome: {nome}")
    print(f"email: {email}")


def enviar_dados_servico():
    nome_servico = dpg.get_value("campo_servico")
    valor_servico = dpg.get_value("campo_valor")
    print(f"Serviço: {nome_servico}")
    print(f"Valor: {valor_servico}")


def gerarPDF():
    nome_servico = dpg.get_value("")
    print(f"Serviço: {nome_servico}")


with dpg.window(label="Emissão de Orçamentos", width=480, height=300, pos=(10, 10)):
    dpg.add_text("Cadastro de Clientes")

    dpg.add_input_text(label="Nome:", tag="campo_nome")

    dpg.add_input_text(label="Email:", tag="campo_email")

    dpg.add_button(label="Cadastra Cliente", callback=enviar_dados_cliente)


with dpg.window(label="Segunda Janela", width=480, height=300, pos=(500, 10)):
    dpg.add_text("Cadastro de Servicos")

    dpg.add_input_text(label="Nome do Servico:", tag="campo_servico")

    dpg.add_input_text(label="Valor:", tag="campo_valor")

    dpg.add_button(label="Cadastra servico", callback=enviar_dados_servico)


with dpg.window(label="Terceira Janela", width=970, height=300, pos=(0, 310)):
    dpg.add_text("Escolha uma opcao para:")
    dpg.add_combo(
        items=["opcao 1", "opcao 2", "opcao 3"],
        default_value="opcao 1",
        label="Menu de Seleção"
    )

    dpg.add_text("Escolha os Serviços")
    dpg.add_checkbox(label="Pick Me",)

    dpg.add_button(label="Gerar PDF", callback=gerarPDF)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
