# coding=utf-8
"""
Longest Common Prefix
~~~~~~~~~~~~~~~~~~~~~

Write a function to find the longest common prefix string amongst an
array of strings.
"""

class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_len = min(len(s) for s in strs)
        p = 0
        for n in xrange(min_len):
            char = strs[0][n]
            for s in strs[1:]:
                if s[n] != char:
                    return strs[0][:p]
            p += 1
        return '' if p == 0 else strs[0][:p]
