# coding=utf-8
"""
chimera.leetcode_2
~~~~~~~~~~~~~~~~~~

Add Two Numbers

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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = node = ListNode(0)
        carry = 0
        while l1 or l2:
            num = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            node.next = ListNode(num % 10)
            carry = num / 10
            l1, l2, node = l1 and l1.next, l2 and l2.next, node.next
        if carry:
            node.next = ListNode(carry)
        return ret.next
