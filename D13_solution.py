"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

s = "abccccccccccccbababab"
k = 2

def kUnique_1(s, k):
	# 1st approach, to be worked on, currently not working
	# set is a powerful tool to be used?
	longest_unique = 0
	s_length = len(s)

	start_ptr = 0
	end_ptr = 0
	cur_longest_start = 0
	cur_longest_end = 0

	lst = []

	while (end_ptr < s_length):
		print(end_ptr)
		if (end_ptr == 0):
			lst.append(s[0])

		if (((len(lst) < k) & (s[end_ptr] not in lst)) or ((len(lst) <= k) & (s[end_ptr] in lst))):
			if ((end_ptr - start_ptr) >= (cur_longest_end - cur_longest_start)):
				start_ptr, end_ptr = cur_longest_start, cur_longest_end
				solution = s[cur_longest_start:cur_longest_end+1]
				print('first')
			if (s[end_ptr] not in lst):
				lst.append(s[end_ptr])
				print('second')
			elif (s[end_ptr] in lst):
				print('third')
				pass
		else:
			print('in else')
			lst.remove(s[start_ptr])
			lst.append(s[end_ptr])
			start_ptr += 1
		print('lst', lst)
		print('sol', solution)
		end_ptr += 1
	return (solution)

def kUnique_2 (s, k):
	# 2nd approach better efficiency and more elegant
	assert (len(s) >= k)

	start_ptr, end_ptr, maxlen = 0, k, k

	while (end_ptr < len(s)):
		end_ptr += 1

		while True:
			print(s[start_ptr:end_ptr])
			distinct_char = len(set(s[start_ptr:end_ptr]))

			if (distinct_char <= k):
				break
			start_ptr += 1
		maxlen = max(maxlen, (end_ptr - start_ptr))
		if ((end_ptr - start_ptr) == maxlen):
			n_s = s[start_ptr:end_ptr]
			# cur_longest_start, cur_longest_end = start_ptr, end_ptr
		print('maxlen', maxlen)
	return (n_s)

print(kUnique_1(s, k))

# 2nd sol t O(n) worst case should be 2n, s O(n) (depends on the length increase)
