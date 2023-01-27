from view import Console
from model import Database

def start():
    c = Console()
    db = Database()

    db.set_class(c.input_class())
    db.set_subject(c.input_subject())
    db.open_file()
    
    while True:
        subject = db.get_subject()
        c.module_name(subject)
        records = db.get_records()
        c.list_of_students(records)        
        
        student = c.who_answers()
        while db.name_checker(student) is False\
            and student != 'exit':
            c.alert_name()
            student = c.who_answers()      
        
        if student == 'exit':
            break

        mark = int(c.what_mark())  
        while db.mark_checker(mark) is False:            
            c.alert_mark()
            mark = int(c.what_mark())   

        db.student_mark(student, mark)
    
    db.save_file()