from homework9.task2.suppressed_exception import Supressor, my_context_manager


class TestClassSupressor:
    def test_class_with_out_error(self):
        with Supressor(Exception):
            result = []
            assert result == []

    def test_class_with_error(self):
        with Supressor(Exception):
            result = [][2]
            assert result


class TestFuncContextManager:
    def test_context_manager_without_error(self):
        with my_context_manager(Exception):
            result = []
            assert result == []

    def test_context_manager_with_error(self):
        with my_context_manager(Exception):
            print('a')
            assert True
