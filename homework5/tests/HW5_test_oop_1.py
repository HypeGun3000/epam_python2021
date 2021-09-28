from unittest.mock import Mock

import pytest

from homework5.task1.oop_1 import Homework, Student, Teacher


class TestOOP1:
    @pytest.fixture
    def create_random_student(self):
        return Student("Bychkov", "Daniil")

    @pytest.fixture
    def create_random_teacher(self):
        return Teacher("Ivanova", "Nadezhda")

    def test_random_student_with_normal_info(self, create_random_student):
        assert create_random_student.first_name == "Daniil"
        assert create_random_student.last_name == "Bychkov"

    def test_random_teacher_with_normal_info(self, create_random_teacher):
        assert create_random_teacher.first_name == "Nadezhda"
        assert create_random_teacher.last_name == "Ivanova"

    def test_student_late_for_homework(self, create_random_student, capsys):
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Tests", 0))
        create_random_student.do_homework(teacher.create_homework())
        out, err = capsys.readouterr()
        assert out == "You are late\n"
