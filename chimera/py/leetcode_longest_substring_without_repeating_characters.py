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
        ret, head = 0, 0
        for inx in range(len(s)):
            if s[inx] in s[head: inx]:
                ret = max(ret, inx - head)
                head = s[:inx].rindex(s[inx]) + 1
        return max(ret, len(s) - head)
