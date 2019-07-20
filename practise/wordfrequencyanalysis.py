# build a working example then simplify the code
import io
class read_from_txt():
	"""docstring for ClassName"""
	def __init__(self):
		self.word_lst = []
		self.wordcount_dict = {}

	def read_txt(self):
		with io.open ("wordfrequencyanalysis.txt", 'r', encoding = 'utf_8') as rf:
			for line in rf:
				line_split = line.split()
				for word in line_split:
					word = word.rstrip(",.?:;")
					# print(word.lower())
					if word.lower() not in self.wordcount_dict:
						self.wordcount_dict[word.lower()] = 1
					elif word.lower() in self.wordcount_dict:
						self.wordcount_dict[word.lower()] += 1
		self.word_lst = self.wordcount_dict.items()
		self.word_lst = sorted(self.word_lst, key = lambda x: x[1])
		print(self.word_lst[:-21:-1])
		# print(self.wordcount_dict)



		
r = read_from_txt()
r.read_txt()