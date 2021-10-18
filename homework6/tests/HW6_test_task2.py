import datetime
from collections import defaultdict

import pytest

from homework6.task2 import oop_2_hw6

student = oop_2_hw6.Student("Ivanov", "Ivan")
teacher = oop_2_hw6.Teacher("Smirnova", "Inna")
hw_end_deadline = oop_2_hw6.Homework("tests2", 0)
homework_result = \
    oop_2_hw6.HomeworkResult(oop_2_hw6.Homework("tests", 3),
                             student, "homework_done")


class TestSchool:
    @pytest.fixture
    def clean_homework(self):
        oop_2_hw6.Teacher.homework_done = defaultdict(set)
        oop_2_hw6.Teacher._homework_db = defaultdict(set)

    def test_error_deadline_end(self):
        with pytest.raises(oop_2_hw6.DeadlineError):
            assert student.do_homework(oop_2_hw6.Homework("tests2", 0),
                                       "homework_done")

    def test_negative_deadline(self):
        with pytest.raises(ValueError):
            assert student.do_homework(oop_2_hw6.Homework("tests3", -3),
                                       "homework_done")

    def test_positive_deadline(self):
        assert student.do_homework(oop_2_hw6.Homework("tests", 3),
                                   "answer_for_all_tasks")

    def test_creating_homework(self):
        create_homework = teacher.create_homework("Test debug", 3)
        assert create_homework.deadline == datetime.timedelta(days=3)
        assert create_homework.text == "Test debug"

    def test_check_homework(self, clean_homework):
        assert teacher.check_homework(homework_result)
        clean_homework

    def test_check_wrong_homework_solution(self, clean_homework):
        assert not teacher. \
                   check_homework(oop_2_hw6.
                                  HomeworkResult(oop_2_hw6.
                                                 Homework("tests", 3),
                                                 student,
                                                 "Pass"))
        clean_homework

    def test_check_wrong_homework_duplicate(self, clean_homework):
        student2 = oop_2_hw6.Student("Shitko", "Roman")
        assert teacher.check_homework(homework_result)
        assert not teacher.check_homework(homework_result)
        assert teacher. \
            check_homework(oop_2_hw6.
                           HomeworkResult(oop_2_hw6.Homework("tests_new", 3),
                                          student2, "new_homework_done"))
        clean_homework

    def test_reset_results_homework(self, clean_homework):
        student2 = oop_2_hw6.Student("Shitko", "Pavel")
        create_homework_2 = teacher.create_homework("Create oop task", 3)
        solution2 = student2.do_homework(create_homework_2, "Done homework")
        teacher.check_homework(homework_result)
        teacher.check_homework(solution2)
        assert len(teacher.homework_done) == 2
        teacher.reset_results()
        assert len(teacher.homework_done) == 0
        clean_homework

    def test_reset_single_result(self, clean_homework):
        homework1 = oop_2_hw6.Homework("Create new fixture", 2)
        student2 = oop_2_hw6.Student("Petrov", "Mikhail")
        homework_result1 = oop_2_hw6.HomeworkResult(homework1,
                                                    student2, "Solution")
        create_homework2 = teacher.create_homework("create web site", 3)
        solution2 = student2.do_homework(create_homework2, "done task")
        teacher.check_homework(homework_result1)
        teacher.check_homework(solution2)
        assert len(teacher.homework_done) == 2
        teacher.reset_results(homework=homework1)
        assert len(teacher.homework_done) == 1
        clean_homework
