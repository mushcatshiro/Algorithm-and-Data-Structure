"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# since its decodable thus not considering any thing larger than 26 and smaller than 1
# since decoding chuncks of 1 or 2 digit integers

from itertools import permutations

dic = {}
ndic = {}
msg = '111'

class mapping:
	def __init__(self, dic):
		self.dic = dic
	def map_ (self):
		i = 0
		while i < 26:
			self.dic[i+1] = chr(97+i)
			i+=1
		return(self.dic)

def chkRange(msg):
	return True if int(msg) < 27 and int(msg) > 0

def solution(msg):
	if len(msg) == 1 and chkRange(msg):
		return 1
	elif len(msg) == 2 and chkRange(msg):
		return 2

		

# enc = mapping(dic)
# dec = decode(msg)
# how to slice
# print(enc.map_())

# get mapping

# first approach

# how long? how general?
# any neighbour sum <27 & >9