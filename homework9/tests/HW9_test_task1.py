from homework9.task1.file_iterator import merge_sorted_files


import pytest


class TestMergeFiles:
    def test_merge_two_files_empty_string(self):
        """Test files with empty strings
        and not int numbers"""
        assert merge_sorted_files(['third.txt', 'fourth.txt']) == [5, 9, 9, 19, 20, 25, 1000]

    def test_not_real_files(self):
        with pytest.raises(FileNotFoundError) as e:
            merge_sorted_files(["asdasfgasg.txt", "asdasf.txt"])
            msg_error = e.value.args[0]
            assert msg_error == "[Errno 2] No such file or directory: 'asdasfgasg.txt'"
