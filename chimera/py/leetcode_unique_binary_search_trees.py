# coding=utf-8
"""
chimera.leetcode_unique_binary_search_trees
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example, given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1, 1, 2]
        if n < 3:
            return ret[n]
        ret.extend(0 for i in xrange(n - 2))
        for i in xrange(3, n + 1):
            for j in xrange(i):
                ret[i] += ret[j] * ret[i - j - 1]
        return ret[-1]
