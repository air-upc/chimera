# coding=utf-8
"""
chimera.leetcode_rotate_list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a list, rotate the list to the right by k places, where k is
non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        tail = p = head
        n = 0
        while tail:
            n += 1
            p = tail
            tail = tail.next
        p.next = head
        rotate = k % n
        for i in xrange(n - rotate):
            p = head
            head = head.next
        p.next = None
        return head
