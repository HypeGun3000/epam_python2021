from datetime import timedelta, datetime


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.now()


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework):
        if homework.is_active() is True:
            return homework
        else:
            print("You are late")


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        return Homework(text, deadline)
