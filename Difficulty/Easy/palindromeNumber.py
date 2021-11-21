"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.
"""


def isPalindrome(self, x: int) -> bool:
    # convert to string and compare reverse
    # return str(x) == str(x)[::-1]
    if x != abs(x):
        return False
    elif x == 0:
        return True
    else:
        temp = x
        reverted_numbers = []
        while temp > 0:
            digit = temp % 10
            reverted_numbers.append(digit)
            temp = temp // 10
        org_numbers = reverted_numbers[::-1]
        return reverted_numbers == org_numbers


print(isPalindrome(any, 121))
print(isPalindrome(any, -121))
print(isPalindrome(any, 10))
print(isPalindrome(any, -101))
