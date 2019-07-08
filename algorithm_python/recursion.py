def rec (x):
	if (x == 10):
		return 10
	else:
		return (x + rec (x+1))

print(rec(0))