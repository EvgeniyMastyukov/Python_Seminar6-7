

def get_process():
    return int(input('Выберите операцию:\nвнести изменения в файл "ученики" - 1;\n'\
        'html представление - 2\n'\
            'вывести на эран список учеников - 3\n'\
                'вывести на эран список телефонов - 4\n' ))

def view():
    with open('school/students.csv','r') as file:
        print(file.read())

def view_tel():
    with open('school/telephone.csv','r') as file:
        print(file.read())