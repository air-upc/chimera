# coding=utf-8
"""
chimera.leetcode_zigzag_conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
    Subscribe to see which companies asked this question.
"""

class Solution(object):

    def convert(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        slen = len(s)
        if slen < num_rows or num_rows <= 1:
            return s
        ret, i = "", 0
        for r in range(0, num_rows):
            i = 0
            while r + (2 * num_rows - 2) * i < slen:
                ret = "".join((ret, s[r + (2 * num_rows - 2) * i]))
                if 0 < r < num_rows - 1:
                    # num_rows * i + num_rows + num_rows - 2 - r \
                    # + i * (num_rows - 2)
                    inx = num_rows * (i + 1) - r + (i + 1) * (num_rows - 2)
                    if inx < slen:
                        ret = "".join((ret, s[inx]))
                i += 1
        return ret
