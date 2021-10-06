from datetime import datetime, timedelta
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Human:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class HomeworkResult:
    def __init__(self, homework, solution: str):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ValueError("homework must be Homework obj")
        self.solution = solution
        self.author = Student
        self.created = datetime.now()


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        if deadline >= 0:
            self.deadline = timedelta(days=deadline)
        else:
            raise ValueError("Deadline must be more than 0")
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline < datetime.now()


class Student(Human):
    def do_homework(self, homework: Homework, solution):
        if homework.is_active():
            raise DeadlineError("You are late")
        else:
            return HomeworkResult(homework, solution)


class Teacher(Human):
    homework_done = defaultdict(list)
    _homework_db = defaultdict(list)

    def check_duplicate(self, homework_result):
        hw_info = (
            homework_result.homework,
            homework_result.solution
        )
        if self._homework_db[homework_result.homework]:
            for homework in self._homework_db[homework_result]:
                print(homework)
                if homework[0] == hw_info[0] and homework[1] == hw_info[1]:
                    return False
        self._homework_db[homework_result.homework].append(hw_info)
        return True


    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result):
        if len(homework_result.solution) > 5 and self.check_duplicate(homework_result):
            self.homework_done[homework_result.homework].append(homework_result)
            return True
        return False



if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'I have done this hw too')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    print(opp_teacher.check_homework(result_1))
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    print(opp_teacher.check_homework(result_2))
    print(opp_teacher.check_homework(result_3))

    print(Teacher.homework_done[oop_hw])
    #Teacher.reset_results()