import datetime
from collections import defaultdict

import pytest


from homework6.task2 import oop_2_hw6

student = oop_2_hw6.Student("Ivanov", "Ivan")
teacher = oop_2_hw6.Teacher("Smirnova", "Inna")
homework1 = oop_2_hw6.Homework("tests", 3)
hw_end_deadline = oop_2_hw6.Homework("tests2", 0)
#hw_negative_deadline = oop_2_hw6.Homework("tests3", -3)
homework_result = oop_2_hw6.HomeworkResult(homework1, student, "homework_done")

class TestSchool:
    def test_error_deadline_end(self):
        with pytest.raises(oop_2_hw6.DeadlineError):
            assert student.do_homework(hw_end_deadline, "homework_done")

