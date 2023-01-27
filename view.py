class Console:
    def input_class(self):
        return input('\nWhat is the class? ').upper()

    def input_subject(self):
        return input('\nWhat is the subject? ').lower()

    def who_answers(self):
        return input('\nWho is going to answer? ')

    def what_mark(self):
        return input('\nWhat is the mark? ')

    def list_of_students(self, records: dict):
        for i, student in enumerate(records, 1):
            print(f'{i}. {student:15} {records.get(student)}') 

    def alert_name(self):
        print('\n---------------------------')
        print('Student is not in the class')
        print('---------------------------')   

    def alert_mark(self):
        print('\n-------------------')
        print('Mark is not correct')
        print('-------------------')  

    def module_name(self, subject: str):
        print('\n--------------------')
        print(f'Subject: {subject}') 
        print('--------------------')                          