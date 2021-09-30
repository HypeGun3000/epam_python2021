from homework4.task3.get_print_output import my_precious_logger


class TestStderrStdout:
    def test_error_if_string_start_with_error(self, capsys):
        my_precious_logger("error of all time")
        out, err = capsys.readouterr()
        assert err == 'error: file not found'

    def test_text_not_start_with_error(self, capsys):
        my_precious_logger("it fine, im ok")
        out, err = capsys.readouterr()
        assert out == "it fine, im ok"
