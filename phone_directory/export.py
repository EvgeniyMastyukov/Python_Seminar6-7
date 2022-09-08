from user_interface import get_first_name
from user_interface import get_last_name
from user_interface import get_tel
from user_interface import get_description
def export_structure1():
    with open('phone_directory/data_phone1.csv', 'a') as file:
        file.write('{}\n{}\n{}\n{}\n\n'\
            .format(get_first_name, get_last_name, get_tel, get_description))


def export_structure2():
    with open('phone_directory/data_phone2.csv', 'a') as file:
        file.write('{},{},{},{}\n'\
            .format(get_first_name, get_last_name, get_tel, get_description))