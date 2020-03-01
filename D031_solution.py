"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them
"""

s_1 = 'kitten'
s_2 = 'sitting'

def editDistance(s_1, s_2):
	l_1 = list(s_1)
	l_2 = list(s_2)

	for i in l_1:
		if i in l_2:
			