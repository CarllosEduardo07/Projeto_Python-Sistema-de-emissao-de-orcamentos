import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='janela', width=1000, height=500)


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


with dpg.window(label="Emissão de Orçamentos", width=480, height=300, pos=(10, 10)):
    dpg.add_text("Cadastro de Clientes")

    dpg.add_input_text(label="Nome:")

    dpg.add_input_text(label="Email:")

    dpg.add_button(label="Cadastra Cliente")

with dpg.window(label="Segunda Janela", width=480, height=300, pos=(500, 10)):
    dpg.add_text("Cadastro de Serviços")

    dpg.add_input_text(label="Nome do Serviço:")

    dpg.add_input_text(label="Valor:")

    dpg.add_button(label="Cadastra serviço")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
