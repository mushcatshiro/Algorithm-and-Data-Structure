"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds
"""

import time

def job_scheduler(f, n):
	time.sleep(n)
	print(f)

def func():
	return (1+3)

job_scheduler(func(), 10)