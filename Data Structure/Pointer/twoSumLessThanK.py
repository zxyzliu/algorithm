"""
Given an array A of integers and integer K, return the maximum S such that
there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation,
return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.

Time complexity : Each of the n elements is visited at most once, thus the time complexity is O(n).

Space complexity : I only use two indexes, the space complexity is O(1).

I can apply brute force directly to get O(n^2) time and O(1) space. But I do not make use of the
property where the input array is sorted.
如果可以sorting的话，就可以考虑使用左右双指针来节约时间。这类题如果不用双指针，直接上两个嵌套的loop循环，面试一定会被
challenge。当使用左右指针法的时候，记得用while loop，不用再用for loop了。
"""


def twoSumLessThanK(arr, target):
    n = -1
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target:
            n = max(n, arr[left] + arr[right])
            left += 1
        else:
            right -= 1
    return n


print(twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60))
