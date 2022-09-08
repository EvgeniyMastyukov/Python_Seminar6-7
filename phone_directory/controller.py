
import user_interface
import export
import importt

def button_click():
    res = user_interface.get_process()
    if res == 1:
        export.export_structure1()
    elif res == 2:
        importt.import_structure1()


