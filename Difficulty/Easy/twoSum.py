"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    hash_table = {}

    for i in range(0, len(nums)):
        temp = target - nums[i]
        if temp in hash_table:
            result.extend([hash_table[temp], i])
        hash_table[nums[i]] = i

    return result


print(twoSum(any, [2, 7, 11, 15], 9))
