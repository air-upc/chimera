# coding=utf-8
"""
chimera.leetcode_add_two_numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """..note:: not change the param node list here; when the param node list
    can be changed, we can use the exists ListNode and save lots of resource.
    """
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            sum = ((l1 and l1.val) or 0) + ((l2 and l2.val) or 0) + carry
            node = ListNode(sum % 10)
            carry = sum / 10
            l1, l2, cur.next, cur = l1 and l1.next, l2 and l2.next, node, node
        cur.next = ListNode(carry) if carry else None
        return ret.next
