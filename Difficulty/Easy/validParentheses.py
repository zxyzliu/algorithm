"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def isValid(self, s: str) -> bool:
    bracket_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []

    for char in s:
        if char in bracket_map:
            stack.append(char)
        elif not stack:
            return False
        else:
            opening = stack.pop()
            closing = bracket_map[opening]
            if char != closing:
                return False
    return not stack


print(isValid(any, "()"))
print(isValid(any, "()[]{}"))
print(isValid(any, "([)]"))
print(isValid(any, "{[]}"))
