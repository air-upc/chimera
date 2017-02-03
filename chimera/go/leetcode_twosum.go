package main

/*
chimera.leetcode_twosum
~~~~~~~~~~~~~~~~~~~~~~~

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9
    Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
*/

import "fmt"

func main() {
	target := 9
	input := []int{2, 7, 11, 15}
	fmt.Printf("The solution is %v\n", twoSum(input, target))
}

func twoSum(nums []int, target int) []int {
	var ret []int
	storage := make(map[int]int, len(nums))
	for index, num := range nums {
		if pre_index, found := storage[target-num]; found {
			ret = []int{pre_index, index}
			break
		} else {
			storage[num] = index
		}
	}
	return ret
}
