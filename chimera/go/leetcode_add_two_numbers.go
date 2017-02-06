package main

/*
chimera.leetcode_add_two_numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	a := &ListNode{1, &ListNode{Val: 8}}
	b := &ListNode{Val: 0}
	fmt.Println(a, b)
	res := addTwoNumbers(a, b)
	fmt.Println(res)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	ret := &ListNode{0, nil}
	cur := ret
	carry := 0
	for l1 != nil || l2 != nil {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		node := &ListNode{sum % 10, nil}
		carry = sum / 10
		cur.Next, cur = node, node
	}
	if carry != 0 {
		cur.Next = &ListNode{carry, nil}
	}
	return ret.Next
}
