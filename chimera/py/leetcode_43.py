# coding=utf-8
"""
chimera.leetcode_43
~~~~~~~~~~~~~~~~~~~

Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return
the product of num1 and num2.

Note:

    1. The length of both num1 and num2 is < 110.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.

You must not use any built-in BigInteger library or convert the inputs to
integer directly.
"""

class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1) * int(num2))
        num1_len, num2_len = len(num1), len(num2)
        num1_bits = [int(b) for b in num1[::-1]]
        num2_bits = [int(b) for b in num2[::-1]]
        res = []
        for inx, bit in enumerate(num2_bits):
            r = [0 for _ in xrange(inx)]
            r.extend(bit * b for b in num1_bits)
            r.extend(0 for _ in xrange(num2_len - inx - 1))
            res.append(r)
        ret = []
        for i in xrange(num1_len + num2_len - 1):
            ret.append(sum(s[i] for s in res))
        for i in xrange(len(ret) - 1):
            ret[i + 1] += ret[i] / 10
            ret[i] = ret[i] % 10
        return ''.join(str(i) for i in ret[::-1]).lstrip('0') or '0'
