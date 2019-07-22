# build a working example then simplify the code
import io
import re

class read_from_txt():
	"""docstring for ClassName"""
	def __init__(self):
		self.word_lst = []
		self.wordcount_dict = {}

	def read_txt(self):
		with io.open ("wordfrequencyanalysis.txt", 'r', encoding = 'utf_8') as rf:
			for line in rf:
				for word in line.split():
					word = s = re.sub(r'[,\.?!:;]','',word)
					# print(word.lower())
					if word.lower() not in self.wordcount_dict:
						self.wordcount_dict[word.lower()] = 1
					elif word.lower() in self.wordcount_dict:
						self.wordcount_dict[word.lower()] += 1
		self.word_lst = self.wordcount_dict.items()
		# in python 3 items() returns a dict_item thus unable to use sort()
		self.word_lst = sorted(self.word_lst, key = lambda x: x[1])
		# print(self.word_lst[::-1])
		# print(self.wordcount_dict)
	def write_txt(self):
		with io.open("test.txt", 'w') as wf:
			for item in self.word_lst:
				wf.write(item[0]+ '\n')


		
r = read_from_txt()
r.read_txt()
r.write_txt()