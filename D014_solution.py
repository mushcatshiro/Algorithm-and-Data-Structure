"""
The area of a circle is defined as pi r^2. Estimate pi to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2
"""

import random

def monteC (num):

	count = 0
	total = 0
	prev_pi, new_pi = 0, 0


	while True:
		for i in range(num):
			if (((random.random()**2) + (random.random()**2)) <= 1):
				count += 1
			total += 1
		prev_pi = new_pi
		new_pi = 4 * ((count)/float(total))
		print('{}, {}'.format(prev_pi, new_pi))
		if (abs(new_pi - prev_pi) < 0.0001):
			return new_pi

print(monteC(1000))

