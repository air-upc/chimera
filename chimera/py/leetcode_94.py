# coding=utf-8
"""
chimera.leetcode_94
~~~~~~~~~~~~~~~~~~~

Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
    Given binary tree [1,null,2,3],
       1
        \
         2
        /
       3
    return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, nodes = [], []
        while root or nodes:
            while root:
                nodes.append(root)
                root = root.left
            node = nodes.pop()
            ret.append(node.val)
            root = node.right
        return ret
