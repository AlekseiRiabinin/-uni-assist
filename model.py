class Database:
    def __init__(self):
        self.records = {}
        self.subject = ''
        self.path = ''

    def set_class(self, class_path: str):
        self.path = '-uni-assist/class_' + class_path + '.txt'

    def set_subject(self, current_subject: str):
        self.subject = current_subject

    def open_file(self):     
        with open(self.path, 'r', encoding='UTF-8') as data:
            file = data.readlines()
        
        for sub in file:
            if sub.split(';')[0] == self.subject:
                for study in sub.split(';')[1].strip().split(', '):
                    self.records[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))               

    def save_file(self):
        new_file = []
        
        with open(self.path, 'r', encoding='UTF-8') as data:
            file = data.readlines()                     
        
        for sub in file:
            if sub.split(';')[0] != self.subject:
                new_file.append(sub.strip())
        
        item = []
        for student, marks in self.records.items():
            item.append(student + ':' + ' '.join(list(map(str, marks))))
        
        item = self.subject + ';' + ', '.join(item)
        new_file.append(item)
        
        with open(self.path, 'w', encoding='UTF-8') as data:
            data.write('\n'.join(new_file))

    def student_mark(self, student: str, mark: int):
        marks = self.records.get(student)
        marks.append(mark)
        self.records[student] = marks

    def name_checker(self, student: str):
        if student not in self.records:
            return False 

    def mark_checker(self, mark: int):
        if mark not in [1, 2, 3, 4, 5]:
            return False            

    def get_records(self):
        return self.records 

    def get_subject(self):

        if self.subject == 'anal':
            message = 'analytics'

        if self.subject == 'math':
            message = 'mathematics'

        if self.subject == 'calc':
            message = 'calculus'

        return message    

