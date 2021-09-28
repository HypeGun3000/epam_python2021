from datetime import datetime, timedelta


class Human:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message


class HomeworkResult:
    def __init__(self, homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.author = Student
        self.created = datetime.now()


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        if deadline >= 0:
            self.deadline = timedelta(days=deadline)
        else:
            raise ValueError("Deadline must be more then 0, or equal 0")
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline < datetime.now()


class Student(Human):
    def do_homework(self, homework: Homework):
        if homework.is_active():
            return homework
        else:
            raise DeadlineError


class Teacher(Human):
    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)
