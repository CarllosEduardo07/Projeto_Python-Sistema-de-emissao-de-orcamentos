import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='janela', width=1200, height=800)

with dpg.window(label="Emissão de Orçamentos", ):
    dpg.add_text("Cadastro de Clientes")
    dpg.add_text("Nome:")
    dpg.add_input_text(label="string", default_value="Nome do Cliente")
    dpg.add_input_text(label="string", default_value="Email")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
    dpg.add_button(label="Save")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
