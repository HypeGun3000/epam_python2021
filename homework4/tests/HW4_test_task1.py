import os

import pytest

from homework4.task1.read_file import read_magic_number


class TestMagicNumber:
    @pytest.fixture
    def create_file_wrong_first_line(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "data.txt")
        test_data = "moommy\n51\n2"
        with open(test_file_path, "w") as file_open:
            file_open.writelines(test_data)
        return test_file_path

    @pytest.fixture
    def create_file_true_first_line(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "data2.txt")
        test_data = "2\n5415wjdglsg"
        with open(test_file_path, "w") as file_open:
            file_open.writelines(test_data)
        return test_file_path

    def test_with_normal_first_line(self, create_file_true_first_line):
        assert read_magic_number(create_file_true_first_line) is True

    def test_with_false_first_line(self, create_file_wrong_first_line):
        with pytest.raises(ValueError):
            assert read_magic_number(create_file_wrong_first_line) is True

    def test_false_first_line(self, create_file_wrong_first_line):
        with pytest.raises(ValueError):
            assert read_magic_number(create_file_wrong_first_line) is True

    def test_false_file_magic_number(self):
        with pytest.raises(ValueError):
            assert read_magic_number("asfasf/sdfasd/asdf") is True
