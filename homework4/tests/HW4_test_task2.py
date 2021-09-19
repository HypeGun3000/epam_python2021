from homework4.task2.mock_input import count_dots_on_i
from unittest.mock import Mock


class TestMockInput:
    def test_count_of_i_in_url(self, monkeypatch):
        url_openmock = Mock()
        url_openmock.read.decode = Mock(return_value="iiirrr")
        monkeypatch.setattr("homework4.task2.mock_input", ("homework4.task2.task.get_text_from_site", url_openmock.read.decode))
        assert count_dots_on_i("xxx") == 3
