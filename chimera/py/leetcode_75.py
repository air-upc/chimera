# coding=utf-8
"""
chimera.leetcode_75
~~~~~~~~~~~~~~~~~~~

Sort Colors

Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        head, tail = 0, len(nums) - 1
        for inx, num in enumerate(nums):
            if num == 2:
                while tail > inx and nums[tail] == 2:
                    tail -= 1
                if inx > tail:
                    break
                nums[inx], nums[tail] = nums[tail], 2
                tail -= 1
            if nums[inx] == 0:
                nums[inx], nums[head] = nums[head], 0
                head += 1
