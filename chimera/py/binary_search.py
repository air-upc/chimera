# coding=utf-8
"""
chimera.binary_search
~~~~~~~~~~~~~~~~~~~~~
"""

def binary_search(seq, target):
    """
    :param seq: ascending sequence
    :param target: target num that in search
    :ret: index if found or None if not found
    """
    head, tail = 0, len(seq) - 1
    while head <= tail:
        # for cython, use
        # mid = head + ((tail - head) / 2)
        mid = (head + tail) >> 1
        num = seq[mid]
        if num == target:
            return mid
        elif num < target:
            head = mid + 1
        else:
            tail = mid - 1
