# coding=utf-8
"""
chimera.leetcode_17
~~~~~~~~~~~~~~~~~~~

Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number
could represent.

Input: Digit string "23"

Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '0': ' ', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        ret = []
        for digit in digits:
            if not ret:
                ret = [lett for lett in mapping[digit]]
                continue
            new = []
            for item in ret:
                new.extend(''.join((item, s)) for s in mapping[digit])
            ret = new
        return ret
