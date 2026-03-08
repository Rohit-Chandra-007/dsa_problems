def reverse_number(n: int) -> int:
    """Reverses the digits of an integer.
    Example: 123 -> 321
    """
    rev = 0
    # Handle negative numbers if needed, but for now matching current logic
    # which assumes positive based on current main.py
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev
