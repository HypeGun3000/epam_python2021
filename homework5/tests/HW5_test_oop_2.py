from unittest.mock import Mock

from homework5.task2.oop2 import print_result


class TestOOP2HW5:
    def test_get_original_docstring_function_name(self):
        func = Mock()
        func.__doc__ = "some docstring"
        func.__name__ = "custom_func"
        decorated_func = print_result(func)
        decorated_func(1, 2, 3)
        assert decorated_func.__doc__ == func.__doc__
        assert decorated_func.__name__ == func.__name__
