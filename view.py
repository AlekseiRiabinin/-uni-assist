def input_class():
    return input('\nWhat is the class? ').upper()

def input_subject():
    return input('\nWhat is the subject? ').lower()

def who_answers():
    return input('\nWho is going to answer? ')

def what_mark():
    return input('\nWhat is the mark? ')

def list_of_students(records: dict):
    for i, student in enumerate(records, 1):
        print(f'{i}. {student:15} {records.get(student)}') 

def alert_name():
    print('\n---------------------------')
    print('Student is not in the class')
    print('---------------------------')   

def alert_mark():
    print('\n-------------------')
    print('Mark is not correct')
    print('-------------------')                           