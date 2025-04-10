import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

with dpg.menu(label="Settings"):
    dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
    dpg.add_menu_item(label="Setting 2", callback=print_me)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
