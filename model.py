records = {}
subject = ''
path = ''

def set_class(class_path: str):
    global path
    path = '-uni-assist/class_' + class_path + '.txt'

def set_subject(current_subject: str):
    global subject
    subject = current_subject

def open_file():
    global records
    global path
    
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                records[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))               

def save_file():
    new_file = []
    
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()                     
    
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    
    item = []
    for student, marks in records.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def student_mark(student: str, mark: int):
    marks = records.get(student)
    marks.append(mark)
    records[student] = marks

def name_checker(student: str):
    if student not in records:
        return False 

def mark_checker(mark: int):
    if mark not in [1, 2, 3, 4, 5]:
        return False            

def get_records():
    return records  
