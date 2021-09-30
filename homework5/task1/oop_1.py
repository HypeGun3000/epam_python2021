from datetime import datetime, timedelta


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


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)
