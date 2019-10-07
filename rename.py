import os
import re
import subprocess

# import sys
# print(sys.version)

# a practise to rename all files name that does not complies to the format D\d{3}_.
# potential need to update to D\d{4}_.

pattern = re.compile('D\d{2}_.')

def list_cwd_py_files(pattern):
	for filename in os.listdir(os.getcwd()):
		if filename.endswith(".py") and pattern.match(filename):
			print(filename)
			subprocess.run(["git", "mv", filename, filename[0:1]+"0"+filename[1:]])
			#os.rename(filename, filename[0:1]+filename[2:])

# list_cwd_py_files(pattern)
subprocess.run(["git", "push", filename, filename[0:1]+"0"+filename[1:]])
# $git mv old_name new_name
# $git commit... git push...
# p1 = subprocess.run('ls')
# print(p1)