import pytest

from homework7.task3.tic_tac_toe import tic_tac_toe_checker


class TestTicTacToe:
    @pytest.fixture
    def vertical_victory_o(self):
        return [["o", "-", "o"], ["o", "x", "o"], ["o", "x", "x"]]

    @pytest.fixture
    def horizontal_victory_x(self):
        return [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]

    @pytest.fixture
    def diagonal_victory_x(self):
        return [["x", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

    @pytest.fixture
    def unfinished(self):
        return [["x", "-", "o"], ["-", "x", "o"], ["x", "o", "-"]]

    @pytest.fixture
    def draw(self):
        return [["x", "o", "o"], ["o", "x", "x"], ["x", "x", "o"]]

    def test_vertical_victory(self, vertical_victory_o):
        assert tic_tac_toe_checker(vertical_victory_o) == 'o wins!'

    def test_horizontal_victory(self, horizontal_victory_x):
        assert tic_tac_toe_checker(horizontal_victory_x) == 'x wins!'

    def test_diagonal_victory(self, diagonal_victory_x):
        assert tic_tac_toe_checker(diagonal_victory_x) == 'x wins!'

    def test_unfinished(self, unfinished):
        assert tic_tac_toe_checker(unfinished) == 'unfinished!'

    def test_draw_result(self, draw):
        assert tic_tac_toe_checker(draw) == 'draw!'
