from .solution import reverse_number

def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(100) == 1
    assert reverse_number(1234) == 4321
    assert reverse_number(0) == 0
