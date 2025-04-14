import dearpygui.dearpygui as dpg

from database.db import get_lista_cliente, get_lista_servicos

# guardando as informações
checkbox_tags_servicos = []  # salva os checkboxes selecionados
servicos_cadastrados = get_lista_servicos()    # pegar os serviços do banco


FRAME_RATE = 60
DELAY_SEGUNDOS = 5
DELAY_FRAMES = DELAY_SEGUNDOS * FRAME_RATE


def mostrar_mensagem(tag_msg, texto, limpar_tags=None):
    dpg.set_value(tag_msg, texto)
    dpg.configure_item(tag_msg, show=True)

    def ocultar():
        dpg.configure_item(tag_msg, show=False)
        if limpar_tags:
            for campo in limpar_tags:
                dpg.set_value(campo, "")

    dpg.set_frame_callback(dpg.get_frame_count() + DELAY_FRAMES, ocultar)


# atualizar o serviços sem fechar a janela
def atualizar_checkboxes_servicos():
    global checkbox_tags_servicos, servicos_cadastrados

    # Limpa os checkboxes anteriores
    for tag in checkbox_tags_servicos:
        dpg.delete_item(tag)

    checkbox_tags_servicos.clear()

    # Recarrega os serviços do banco
    servicos_cadastrados = get_lista_servicos()

    # Adiciona novamente os checkboxes
    for i, servico in enumerate(servicos_cadastrados):
        tag = f"checkbox_servico_{i}"
        checkbox_tags_servicos.append(tag)
        dpg.add_checkbox(
            label=f"{servico[1]} - R${servico[2]:.2f}",
            tag=tag,
            parent="grupo_checkboxes"
        )


# atualizar o nomes dos clientes cadastrados na interface
def atualizar_select_clientes():
    nome_clientes = get_lista_cliente()
    nomes = [cliente[1] for cliente in nome_clientes]
    dpg.configure_item("select_cliente", items=nomes)


def atualizar_interface():
    atualizar_select_clientes()
    atualizar_checkboxes_servicos()
