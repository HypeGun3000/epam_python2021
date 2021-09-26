from unittest.mock import Mock

import pytest

from homework4.task2.mock_input import count_dots_on_i


class TestCountDotsOnUrl:
    def test_find_count_letter(self, monkeypatch):
        urlopen_mock = Mock()
        urlopen_mock.read.decode = Mock(return_value="iiieee")
        monkeypatch.setattr("homework4.task2.mock_input.get_body", urlopen_mock.read.decode)
        assert count_dots_on_i("xxxx") == 3

    def test_is_exist_url(self):
        with pytest.raises(ValueError) as e:
            count_dots_on_i("http://wewwwewe.com/")
        msg = e.value.args[0]
        assert msg == "url doesn't exist"
