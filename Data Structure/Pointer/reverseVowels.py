"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


def reverseVowels(s):
    v = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] in v and s[right] in v:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in v and s[right] not in v:
            right -= 1
        elif s[left] not in v and s[right] in v:
            left += 1
        else:
            left += 1
            right -= 1
    return "".join(s)


print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
