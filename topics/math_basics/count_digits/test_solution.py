from .solution import count_digits, count_digits_divisible


def test_count_digits_divisible():
    assert count_digits(345) == 3  # 3 and 5 divide 345, 4 does not
    assert count_digits(12) == 2  # 1 and 2 divide 12
    assert count_digits(1012) == 4  # 1, 1, and 2 divide 1012
