import math

def prime(i):
	n=2
	if i == 1:
		return False
	while n<=math.sqrt(i):
	
		if i % n == 0:
			return False
		i+=1
	return True

