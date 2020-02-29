"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""

reference = {"{": "}", "[": "]", "(": ")"}

string_1 = "([])[]({})"
string_2 = "([)]"
string_3 = "((()"

def BracketsBalanceCheck(string, reference):
	queue = []

	# for i in string:
	# 	if i in reference:
	# 		queue.append(i)
	# 	else:
	# 		for j, k in enumerate(queue):
	# 			if reference[k] == i:
	# 				queue.pop(j)

	for index, char in enumerate(string):
		if char in reference:
			queue.append(char)
		else:
			if reference[queue[len(queue) - 1]] == char:
				queue.pop()

	if len(queue) == 0:
		return True
	else:
		return False

print(BracketsBalanceCheck(string_2, reference))

# problem with this approach string_2 still escapes, no checks on order inplace
# better approach should have two pointers? <- nope
# better approach should be checking stack[n]
# time complexity O(n)
# space complexity O(n)