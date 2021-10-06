from homework7.task1.find_in_tree import find_occurrences, example_tree


class TestTree:
    def test_example_tree(self):
        assert find_occurrences(example_tree, "RED") == 10

    def test_example_tree_with_wrong_color(self):
        assert find_occurrences(example_tree, "PURPLE") == 0
