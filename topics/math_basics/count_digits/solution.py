def count_digits_divisible(n: int) -> int:
    """Counts the number of digits in n that evenly divide n.
    Example: 121 -> 2 (1 divides 121 twice, 2 does not)
    """
    original = n
    count = 0
    while n > 0:
        rem = n % 10
        if rem != 0 and original % rem == 0:
            count += 1
        n = n // 10
    return count


def count_digits(n: int) -> int:
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
