# coding=utf-8

"""
chimera.leetcode_longest_palindromic_substring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.

Example:

    Input: "cbbd"

    Output: "bb"
"""

class Solution(object):

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str

        As 'aba' and 'abba' are palindromes, we fold the duplicate char first
        to simplify the char-compare logic. e.g. for 'abba', we use
            [[a, 1], [b, 2], [a, 1]]
        to replace it. Then we check the simple replacing list to get the max
        len palindrome.
        """
        ret = ""
        chars = [[s[0], 1]]
        for char in s[1:]:
            if char == chars[-1][0]:
                chars[-1][-1] += 1
            else:
                chars.append([char, 1])
        chars_len = len(chars)
        for index, tup in enumerate(chars):
            substr = tup[0] * tup[-1]
            for n in xrange(1, min(index, chars_len - index - 1) + 1):
                if chars[index - n] == chars[index + n]:
                    new = chars[index - n][0] * chars[index - n][-1]
                    substr = "".join((new, substr, new))
                else:
                    if chars[index - n][0] == chars[index + n][0]:
                        new = chars[index - n][0] * min(chars[index - n][-1],
                                                        chars[index + n][-1])
                        substr = "".join((new, substr, new))
                    break
            if len(substr) > len(ret):
                ret = substr
        return ret
