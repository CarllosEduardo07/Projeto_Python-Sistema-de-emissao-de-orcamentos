import dearpygui.dearpygui as dpg

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
