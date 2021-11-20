"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


Time complexity: Because, for each element, I try to find its complement by looping through the rest
of array which takes O(n) time. Therefore, the time complexity is O(n^2).

Space complexity：O(1)
"""
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    hash_table = {}

    for i in range(0, len(nums)):
        res = target - nums[i]
        if res in hash_table:
            result.extend([nums[i], res])
        hash_table[nums[i]] = nums[i]

    # if we want to print the position
    # for i in range(0, len(nums)):
    #     res = target - nums[i]
    #     if res in hash_table:
    #         result.extend([hash_table[res], i])
    #     hash_table[nums[i]] = i

    return result


print(twoSum(any, [3, 5, 2, -4, 8, 11], 7))


