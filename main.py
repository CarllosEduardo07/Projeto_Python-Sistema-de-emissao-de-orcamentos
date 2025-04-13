import dearpygui.dearpygui as dpg
from src.ui import construir_interface


dpg.create_context()
dpg.create_viewport(title='Sistema de Orçamentos', width=1000, height=650)

construir_interface()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
