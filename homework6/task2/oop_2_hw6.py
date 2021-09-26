from datetime import timedelta, datetime


class Human:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.now()


class Student(Human):
    def do_homework(self, homework: Homework):
        if homework.is_active() is True:
            return homework
        raise DeadlineError("You are late")


class Teacher(Human):
    def create_homework(self, text, deadline):
        return Homework(text, deadline)


class HomeworkResult:
    def __init__(self, homework, solution, author, created):
        if not isinstance(homework, Homework):
            print("You gave a not Homework object")
        self.solution = solution
        self.author = Student
        self.created = datetime.now()

