"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
	# def pair(f):
	# 	return (a, b)
	# return pair
	return (a,b)

def car(pair):
	car, cdr = pair
	print(car)
	return car

def cdr(pair):
	car, cdr = pair
	return cdr

car(cons((3,4),4))

# T O(1)