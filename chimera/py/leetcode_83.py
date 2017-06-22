# coding=utf-8
"""
chimera.leetcode_83
~~~~~~~~~~~~~~~~~~~

Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,

Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret, n = head, head and head.next
        while n:
            if head.val != n.val:
                head.next = n
                head = head.next
            n = n.next
        if head:
            head.next = None
        return ret
