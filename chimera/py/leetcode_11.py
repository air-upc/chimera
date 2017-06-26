# coding=utf-8
"""
chimera.leetcode_11
~~~~~~~~~~~~~~~~~~~

Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        head, tail = 0, len(height) - 1
        while head < tail:
            min_h = min(height[head], height[tail])
            ret = max((tail - head) * min_h, ret)
            if height[head] < height[tail]:
                while head < tail and height[head] <= min_h:
                    head += 1
            else:
                while head < tail and height[tail] <= min_h :
                    tail -= 1
        return ret
