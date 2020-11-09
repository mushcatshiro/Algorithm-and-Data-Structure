"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid
"""

d = {}

s = "AAAABBBCCDAA"
s_2 = "AAAAABBBBCDEFFFFFFFF"

decoded = ""

for c in s:
	print(d)
	if c not in d and len(d) < 2:
		d[c] = 1
		if len(d) == 2:
			t = [x for x in d.items()]
			tmp = str(t[0][1])+str(t[0][0])
			decoded += tmp
			d.pop(t[0][0])
	elif c in d and len(d) < 2:
		d[c] += 1

print(decoded)

# not the most elagant approach
# time complexity O(n)
# space complexity O(n)