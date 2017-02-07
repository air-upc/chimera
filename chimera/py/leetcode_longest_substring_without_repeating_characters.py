# coding=utf-8
"""
chimera.leetcode_longest_substring_without_repeating_characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a string, find the length of the longest substring without repeating
characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the
    answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        index = {}
        sentry = 0
        for inx, cha in enumerate(s):
            if cha not in index:
                ret = max(ret, inx - sentry + 1)
            else:
                if sentry > index[cha]:
                    ret = max(ret, inx - sentry + 1)
                else:
                    sentry = index[cha] + 1
            index[cha] = inx
        return ret
