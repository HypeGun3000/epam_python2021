import os

import pytest

from homework8.task1.dict_file_checker import KeyValueStorage

FILE_PATH = os.path.join(os.getcwd(), "test1.txt")


class TestDictFileChecker:

    x = KeyValueStorage(FILE_PATH)

    def test_new_methods_from_file(self):
        assert self.x.power == 9001

    def test_get_value_from_file(self):
        assert self.x['name'] == 'kek'

    def test_method_incorrect_method(self):
        with pytest.raises(ValueError) as error:
            print(self.x.wrong_attribute)
        assert error.value.args[0] == "Wrong attribute"
