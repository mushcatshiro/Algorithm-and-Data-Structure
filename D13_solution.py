"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

s = "abcba"
k = 2

l = []

for i in range(len(s)):
	if s[i] not in l:
		l.append(s[i])


