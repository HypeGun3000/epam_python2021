import os

import pytest

from homework4.task1.read_file import check_file, read_magic_number


class TestMagicNumber:
    @pytest.fixture
    def create_file_with_wrong_first_line(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "data.txt")
        test_data = "moommy\n51\n2"
        with open(test_file_path, "w") as file_open:
            file_open.writelines(test_data)
        return test_file_path

    @pytest.fixture
    def create_file_with_true_first_line(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "data2.txt")
        test_data = "2\n5415wjdglsg"
        with open(test_file_path, "w") as file_open:
            file_open.writelines(test_data)
        return test_file_path

    def test_if_file_with_wrong_first_line_created(self,
                                            create_file_with_wrong_first_line):
        assert check_file(create_file_with_wrong_first_line) is True

    def test_if_file_with_true_first_line_created(self,
                                            create_file_with_true_first_line):
        assert check_file(create_file_with_true_first_line) is True

    def test_with_normal_first_line(self, create_file_with_true_first_line):
        assert read_magic_number(create_file_with_true_first_line) is True

    def test_with_false_first_line(self, create_file_with_wrong_first_line):
        assert read_magic_number(create_file_with_wrong_first_line) is None

    def test_not_real_file(self):
        assert check_file("asdasd/asdasd/fwqww") is False
