from homework2.list_combinations import combinations


def test_simple_combination():
    assert combinations([1, 2], [3, 4], [5, 6]) == [[1, 3, 5],
                                                    [1, 3, 6],
                                                    [1, 4, 5],
                                                    [1, 4, 6],
                                                    [2, 3, 5],
                                                    [2, 3, 6],
                                                    [2, 4, 5],
                                                    [2, 4, 6]]


def test_heavy_combinations():
    assert combinations([1, 2], [3, 4], [5], [6, 7, 8]) == [[1, 3, 5, 6],
                                                            [1, 3, 5, 7],
                                                            [1, 3, 5, 8],
                                                            [1, 4, 5, 6],
                                                            [1, 4, 5, 7],
                                                            [1, 4, 5, 8],
                                                            [2, 3, 5, 6],
                                                            [2, 3, 5, 7],
                                                            [2, 3, 5, 8],
                                                            [2, 4, 5, 6],
                                                            [2, 4, 5, 7],
                                                            [2, 4, 5, 8]]
