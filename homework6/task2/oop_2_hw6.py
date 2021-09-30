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
    def do_homework(self, homework: Homework):
        if homework.is_active():
            return homework
        else:
            raise DeadlineError("You are late")


class Teacher(Human):
    homework_done = defaultdict(HomeworkResult)

    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result):
        if len(homework_result.solutuion) < 5:
            return False
        else:
            if HomeworkResult not in homework_done[Homework]:
                homework_done[Homework] = HomeworkResult


