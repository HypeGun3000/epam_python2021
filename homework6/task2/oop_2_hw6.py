from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message
        super().__init__(self.message)


class HomeworkResult:
    def __init__(self, homework, student, solution: str):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ValueError("homework must be Homework obj")
        self.solution = solution
        self.author = student
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
        return self.created + self.deadline > datetime.now()


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework, solution):
        student = Student.__call__(self.last_name, self.first_name)
        if homework.is_active():
            return HomeworkResult(homework, student,  solution)
        else:
            raise DeadlineError


class Teacher(Student):
    homework_done = defaultdict(list)
    _homework_db = defaultdict(list)

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
        if self._homework_db[homework_result.homework]:
            for homework in self._homework_db[homework_result.homework]:
                if homework[0] == homework_info[0] or \
                        homework[1] == homework_info[1]:
                    return False
        self._homework_db[homework_result.homework].append(homework_info)
        return True

    def create_homework(self, text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result):
        if len(homework_result.solution) > 5 and\
                self.check_duplicate(homework_result):
            self.homework_done[homework_result.homework].append(homework_result) #E501
            return True
        return False

    @classmethod
    def reset_results(cls, **kwargs):
        if not kwargs:
            cls.homework_done = defaultdict(list)
            cls._homework_db = defaultdict(list)
        else:
            key = list(kwargs.keys())[0]
            del cls.homework_done[kwargs[key]]
            del cls._homework_db[kwargs[key]]
