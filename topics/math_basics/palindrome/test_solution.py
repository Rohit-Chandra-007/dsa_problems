from .solution import isPalindrome, isPalindromeOptimized, isPalindromeTwoPointer


def test_isPalindrome():
    assert isPalindrome(121)
    assert isPalindrome(1001)
    assert not isPalindrome(123)
    assert isPalindromeTwoPointer(121)
    assert isPalindromeTwoPointer(1001)
    assert not isPalindromeTwoPointer(123)
    assert isPalindromeOptimized(121)
    assert isPalindromeOptimized(1001)
    assert not isPalindromeOptimized(123)
