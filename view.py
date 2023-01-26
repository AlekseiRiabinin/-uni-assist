def input_class():
    return input('What is the class? ').upper()

def input_subject():
    return input('What is the subject? ').lower()

def who_answers():
    return input('Who is going to answer? ')

def what_mark():
    return input('What is the mark? ')

def list_of_students(records: dict):
    for i, student in enumerate(records, 1):
        print(f'{i}, {student: 20} {records.get(student)}')