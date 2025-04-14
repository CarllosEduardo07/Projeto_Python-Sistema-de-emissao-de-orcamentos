import dearpygui.dearpygui as dpg
from src.callbacks import cadastrar_dados_cliente, cadastrar_dados_servico, gerar_servico, checkbox_tags_servicos

from database.db import *


def construir_interface():
    with dpg.window(label="Cadastro de Clientes", width=480, height=300, pos=(10, 10)):
        dpg.add_input_text(label="Nome", tag="campo_nome")
        dpg.add_input_text(label="Email", tag="campo_email")
        dpg.add_button(label="Cadastrar Cliente",
                       callback=cadastrar_dados_cliente)
        dpg.add_text("", tag="mensagem_cliente", show=False, color=[0, 200, 0])

    with dpg.window(label="Cadastro de Serviços", width=480, height=300, pos=(500, 10)):
        dpg.add_input_text(label="Nome do Serviço", tag="campo_servico")
        dpg.add_input_text(label="Valor", tag="campo_valor")
        dpg.add_button(label="Cadastrar Serviço",
                       callback=cadastrar_dados_servico)
        dpg.add_text("", tag="mensagem_servico", show=False, color=[0, 200, 0])

    # gerar PDF
    with dpg.window(label="Geração de PDF", width=970, height=300, pos=(0, 310)):

        nome_clientes_cadastrados = get_lista_cliente()

        nomes = [nome[1] for nome in nome_clientes_cadastrados]
        dpg.add_text("Selecione o nome do cliente:")

        dpg.add_combo(items=nomes, label="Selecione um Cliente",
                      tag="select_cliente")

    # ==========================================================================================

       # Cria um grupo de checkboxes
        with dpg.group(tag="grupo_checkboxes"):
            # Obtém os serviços cadastrados no banco
            servicos_cadastrados = get_lista_servicos()
            for i, servico in enumerate(servicos_cadastrados):
                tag = f"checkbox_servico_{i}"
                # Armazena a tag do checkbox para referência futura
                checkbox_tags_servicos.append(tag)

                dpg.add_checkbox(
                    label=f"{servico[1]} - R${servico[2]:.2f}",
                    tag=tag,
                    parent="grupo_checkboxes"  # Especifica o grupo onde os checkboxes serão adicionados
                )

        # Adiciona o botão para gerar o PDF
        dpg.add_button(label="Gerar PDF", callback=gerar_servico)
        dpg.add_text("", tag="mensagem_pdf", show=False, color=[0, 200, 0])
