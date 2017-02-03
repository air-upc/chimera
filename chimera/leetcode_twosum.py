# coding=utf-8
"""
chimera.leetcode_twosum
~~~~~~~~~~~~~~~~~~~~~~~

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9
    Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""


class Solution(object):
    # Change twoSum to two_sum
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storage = {num: index for index, num in enumerate(nums)}
        for index, num in enumerate(nums):
            # sup = target - num
            # if target - num in storage and index != storage[target - num]:
            #    return [index, storage[sup]]
            if target - num in storage and index != storage[target - num]:
                return [index, storage[target - num]]
