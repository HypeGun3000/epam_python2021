from collections import defaultdict
from datetime import datetime, timedelta


class Human:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message
        super().__init__(self.message)


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        if deadline >= 0:
            self.deadline = timedelta(days=deadline)
        else:
            raise ValueError("Deadline must be more than 0")
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.now()


class Student(Human):
    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(homework,
                                  Student(
                                      self.last_name,
                                      self.first_name),
                                  solution
                                  )
        else:
            raise DeadlineError


class HomeworkResult:
    def __init__(self, homework: Homework, student: Student, solution: str):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ValueError("homework must be Homework obj")
        self.solution = solution
        self.author = student
        self.created = datetime.now()


class Teacher(Human):
    homework_done = defaultdict(set)

    def check_duplicate(self, homework_result):
        author_info = (
            f'{homework_result.author.last_name} '
            f'{homework_result.author.first_name}'
        )
        homework_info = (
            author_info,
            homework_result.solution,
            homework_result.homework.text,
        )
        for i in homework_info:
            if i in self.homework_done[homework_result.homework]:
                return False
        for i in homework_info:
            self.homework_done[homework_result.homework].add(i)
        return True

    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result):
        if len(homework_result.solution) > 5 and \
                self.check_duplicate(homework_result):
            self.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, **kwargs):
        if not kwargs:
            cls.homework_done = defaultdict(set)
        else:
            key = list(kwargs.keys())[0]
            del cls.homework_done[kwargs[key]]
