# coding=utf-8
"""
chimera.leetcode_82
~~~~~~~~~~~~~~~~~~~

Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,

Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        ret = r = ListNode(None)
        p = None
        while head:
            if (not p or p.val != head.val) and \
                    (not head.next or head.val != head.next.val):
                r.next = head
                r = r.next
            p = head
            head = head.next
        r.next = None
        return ret.next
