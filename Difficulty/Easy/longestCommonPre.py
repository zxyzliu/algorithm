"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]
    for i in strs[1:]:
        j = len(prefix)
        while prefix != i[:j] and j > 0:
            prefix = prefix[0:j - 1]
            j -= 1
        if prefix == "":
            return "There is no common prefix"
    return prefix


print(longestCommonPrefix(any, ["flower", "flow", "flight"]))
print(longestCommonPrefix(any, ["dog", "racecar", "car"]))
