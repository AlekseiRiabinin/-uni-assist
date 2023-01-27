import view
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    
    while True:
        records = model.get_records()
        view.list_of_students(records)        
        
        student = view.who_answers()
        while model.name_checker(student) is False\
            and student != 'exit':
            view.alert_name()
            student = view.who_answers()      
        
        if student == 'exit':
            break

        mark = int(view.what_mark())  
        while model.mark_checker(mark) is False:            
            view.alert_mark()
            mark = int(view.what_mark())   

        model.student_mark(student, mark)
    
    model.save_file()