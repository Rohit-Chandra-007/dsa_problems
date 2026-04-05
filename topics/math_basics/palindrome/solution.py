def isPalindrome(n: int) -> bool:
    """This Complexity O(n)"""
    number = str(n)
    rev = ""
    for i in range(len(number) - 1, -1, -1):
        rev += number[i]
    return number == rev


def isPalindromeTwoPointer(n: int) -> bool:
    """This Complexity O(n/2)"""
    number = str(n)
    left = 0
    right = len(number) - 1
    while left < right:
        if number[left] != number[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindromeOptimized(n: int) -> bool:
    """ This has Time Complexity O(logn)"""
    original = n
    rev = 0
    while n > 0:
        rev = 10 * rev + n % 10
        n = n // 10
    return original == rev
