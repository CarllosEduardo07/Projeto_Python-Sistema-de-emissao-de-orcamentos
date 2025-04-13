import dearpygui.dearpygui as dpg
from src.ui import construir_interface
from database.db import *

init_db()
dpg.create_context()
dpg.create_viewport(title='Sistema de Orcamentos', width=1000, height=650)

construir_interface()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
