import urllib
from unittest.mock import Mock

import pytest

from homework4.task2.mock_input import count_dots_on_i


class TestCountDotsOnUrl:
    def test_find_count_letter(self, monkeypatch):
        monkeypatch.setattr("homework4.task2.mock_input.get_body",
                            Mock(return_value="iiieee"))
        assert count_dots_on_i("xxxx") == 3

    def test_not_exist_url(self):
        with pytest.raises(urllib.error.URLError):
            assert count_dots_on_i("https://asfas3332221fas.com") is True
