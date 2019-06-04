"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""
dic = {}
ndic = {}

class mapping:
	def __init__ (self, dic):
		self.dic = dic
	def map_ (self):
		i = 0
		while i < 26:
			self.dic[i+1] = chr(97+i)
			i+=1
		return(self.dic)

enc = mapping(dic)
print(enc.map_())

# get mapping

# first approach

# how long? how general?
# any neighbour sum <27 & >9