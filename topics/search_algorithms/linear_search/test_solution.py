from .solution import linear_search


def test_linear_search_found():
    assert linear_search([4, 7, 1, 9], 1) == 2


def test_linear_search_first_match():
    assert linear_search([2, 5, 2, 8], 2) == 0


def test_linear_search_missing():
    assert linear_search([4, 7, 1, 9], 3) == -1


def test_linear_search_empty_array():
    assert linear_search([], 10) == -1
