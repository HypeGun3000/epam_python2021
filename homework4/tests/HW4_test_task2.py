import urllib
from unittest.mock import Mock

from homework4.task2.mock_input import count_dots_on_i


class TestCountDotsOnUrl:
    def test_find_count_letter(self, monkeypatch):
        urlopen_mock = Mock()
        urlopen_mock.read.decode = Mock(return_value="iiieee")
        monkeypatch.setattr("homework4.task2.mock_input.get_body",
                            Mock(return_value="iiieee"))
        assert count_dots_on_i("xxxx") == 3

    def test_not_exist_url(self):
        try:
            count_dots_on_i("http://wewwwewe.com/")
        except urllib.error.URLError:
            print("test passed")
