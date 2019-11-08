"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twosum(arr, s):
    sum = []
    hash_table = {}

    for i in range(0, len(arr)):
        target = s - arr[i]
        if target in hash_table:
            sum.append([arr[i], target])
        hash_table[arr[i]] = arr[i]
    return sum


print(twosum([3, 5, 2, -4, 8, 11], 7))
