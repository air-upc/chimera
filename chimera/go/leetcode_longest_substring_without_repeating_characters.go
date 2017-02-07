package main

/*
chimera.leetcode_longest_substring_without_repeating_characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a string, find the length of the longest substring without repeating
characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the
    answer must be a substring, "pwke" is a subsequence and not a substring.
*/

import "fmt"

func main() {
	s := "abcabcabc"
	fmt.Println(lengthOfLongestSubstring(s))
}

func lengthOfLongestSubstring(s string) int {
	ret := 0
	index := make(map[rune]int, len(s))
	sentry := 0
	for inx, str := range s {
		if i, ok := index[str]; ok {
			if i < sentry {
				num := inx - sentry + 1
				if num > ret {
					ret = num
				}
			} else {
				sentry = index[str] + 1
			}
		} else {
			num := inx - sentry + 1
			if num > ret {
				ret = num
			}
		}
		index[str] = inx
	}
	return ret
}
