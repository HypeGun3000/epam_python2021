import os

import pytest
from homework4.task1.read_file import check_file, read_magic_number


class TestMagicNumber:
    @pytest.fixture
    def create_file_with_wrong_fl(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "data.txt")
        test_data = "moommy\n51\n2"
        with open(test_file_path, "w") as file_open:
            file_open.writelines(test_data)
            return test_file_path

    @pytest.fixture
    def create_file_with_true_fl(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "data2.txt")
        test_data = "2\n5415wjdglsg"
        with open(test_file_path, "w") as file_open:
            file_open.writelines(test_data)
            return test_file_path

    def test_if_file_with_wrong_fl_created(self, create_file_with_wrong_fl):
        assert check_file(create_file_with_wrong_fl)

    def test_if_file_with_true_fl_created(self, create_file_with_true_fl):
        assert check_file(create_file_with_true_fl)

    def test_with_normal_fl(self, create_file_with_true_fl):
        assert read_magic_number(create_file_with_true_fl) is True

    def test_with_false_fl(self, create_file_with_wrong_fl):
        assert read_magic_number(create_file_with_wrong_fl) is None
