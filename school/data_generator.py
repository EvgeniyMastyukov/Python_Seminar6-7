
from editor import get_changes

def add_students():
    data = get_changes().split(',')
    for i in data:
        with open('school/students.csv', 'a') as file:
            file.write('- {};'\
                .format(i))
    return data            

