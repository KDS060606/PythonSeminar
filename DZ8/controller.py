import view
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student != 'Иванов Иван' or student != 'Васильев Василий' or student != 'Петров Петр':
             print("Такого ученика нет в классе")
             student = view.who_answer()
        if student == 'exit':
                break
        mark = int(view.what_mark())
        if mark > 5: print("Введите оценку от 1 до 5")
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()