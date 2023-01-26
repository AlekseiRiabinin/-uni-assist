import view
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        records = model.get_records()
        view.list_of_students(records)
        student = view.who_answers()
        if student == 'exit':
            break
        mark = int(view.what_mark()
        model.student_mark(student, mark))
    model.save_file()