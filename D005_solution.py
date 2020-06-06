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

# cdr(car(cons((3,4),4)))

# T O(1)

# to not ignore the fact that cons returned a function not a value
# car(cons(3, 4)) returns 3
def cons_(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car_(f):
    def left(a, b):
        return a
    return f(left)

def cdr_(f):
    def right(a, b):
        return b
    return f(right)

print(car_(cons_(3, 4)))

# pair(left) => left(a, b) => a