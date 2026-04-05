from .solution import (
    binary_search,
    first_occurrence,
    last_occurrence,
    lower_bound,
    upper_bound,
)


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3


def test_binary_search_missing():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_first_occurrence_found():
    assert first_occurrence([1, 2, 2, 2, 5], 2) == 1


def test_first_occurrence_missing():
    assert first_occurrence([1, 3, 5, 7], 4) == -1


def test_last_occurrence_found():
    assert last_occurrence([1, 2, 2, 2, 5], 2) == 3


def test_last_occurrence_missing():
    assert last_occurrence([1, 3, 5, 7], 4) == -1


def test_lower_bound_found():
    assert lower_bound([1, 2, 2, 2, 5], 2) == 1


def test_lower_bound_insertion_index():
    assert lower_bound([1, 2, 4, 5], 3) == 2


def test_upper_bound_found():
    assert upper_bound([1, 2, 2, 2, 5], 2) == 4


def test_upper_bound_end_index():
    assert upper_bound([1, 2, 4, 5], 5) == 4
