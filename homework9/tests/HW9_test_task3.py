from pathlib import Path

import pytest

from homework9.task3.count_tokenaizer import universal_file_counter


class TestUniFileCounter:
    test_dir = Path(__file__).parents[0]

    def test_files_without_tokens(self):
        assert universal_file_counter(self.test_dir, "txt") == 11

    def test_files_with_token(self):
        assert universal_file_counter(self.test_dir, "txt", str.split) == 9

    def test_not_real_directory(self):
        with pytest.raises(NotADirectoryError) as error:
            assert universal_file_counter("asdasd/afasf/iew", "txt")
        err_msg = error.value.args[0]
        assert err_msg == "It's not a directory"
