"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


def reverseString(s):
    left, right = 0, len(s) - 1
    char_array = list(s)
    result = ""
    while left < right:
        char_array[left], char_array[right] = char_array[right], char_array[left]
        left += 1
        right -= 1
    return result.join(char_array)


print(reverseString("hello"))
