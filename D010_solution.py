"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds
"""

import time

def job_scheduler(**kwargs):
    time.sleep(kwargs['n'])
    def _job_scheduler(f):
        return f
    return _job_scheduler

@job_scheduler(n=2)
def func(num):
    print(num)

# job_scheduler(func, 2)

func(3)
func(5)