from user_interface import get_first_name
from user_interface import get_last_name
from user_interface import get_tel
from user_interface import get_description
def export_structure1():
    first_name = get_first_name()
    last_name = get_last_name()
    tel = get_tel()
    description = get_description()
    with open('phone_directory/data_phone1.csv', 'a') as file:
        file.write('{}\n{}\n{}\n{}\n\n'\
            .format(first_name, last_name, tel, description))

                     
def export_structure2():
    first_name = get_first_name()
    last_name = get_last_name()
    tel = get_tel()
    description = get_description()
    with open('phone_directory/data_phone2.csv', 'a') as file:
        file.write('{},{},{},{}\n'\
            .format(first_name, last_name, tel, description))