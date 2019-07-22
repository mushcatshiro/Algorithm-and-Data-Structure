"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

# first approach

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
	print(cdr)
	return cdr

cdr(car(cons((3,4),4)))

# T O(1)

# second approach, to not ignore the fact that return pair is returned as a function call not a value