"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: -120
Output: -21

"""


def reverse(x):
    num = 0
    a = abs(x)
    while a != 0:
        temp = a % 10
        num = num * 10 + temp
        a = a // 10
    if x > 0 and num < 2 ** 31:
        return num
    elif x < 0 and num <= 2 ** 31:
        return -num
    else:
        return 0


print(120 // 10)
print(reverse(-120))
