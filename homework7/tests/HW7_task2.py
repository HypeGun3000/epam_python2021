from homework7.task2.backspace_equal import backspace_compare


class TestTask2:
    def test_equal_str(self):
        assert backspace_compare("ab#c", "ad#c") is True

    def test_not_equal_str(self):
        assert backspace_compare("a#c", "b") is False

    def test_equal_str_with_backspaces_at_start(self):
        assert backspace_compare("a##c", "#a#c") is True

    def test_equal_str_with_backspaces_in_the_end(self):
        assert backspace_compare("abcd#", "abce#") is True

    def test_str_with_only_backspaces(self):
        assert backspace_compare("#####", "######") is True
