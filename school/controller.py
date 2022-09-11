import editor
import data_generator
from user_interface import get_process
import html_creater
from user_interface import view
import user_interface as user
from user_interface import view_tel

def button_click():
    process = user.get_process()
    if process == 1:
        data_generator.add_students()
    elif process == 2:
        html_creater.create()
    elif process == 3:
        view()
    elif process == 4:
        view_tel()


