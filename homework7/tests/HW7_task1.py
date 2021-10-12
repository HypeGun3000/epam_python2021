from homework7.task1.find_in_tree import example_tree, find_occurrences


def test_example_tree_with_occurence_in_values():
    assert find_occurrences(example_tree, "RED") == 12


def test_example_tree_with_wrong_occurence():
    assert find_occurrences(example_tree, "PURPLE") == 0


def test_example_tree_with_occurence_in_keys():
    assert find_occurrences(example_tree, "jhl") == 4
