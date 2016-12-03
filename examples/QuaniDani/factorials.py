
def iter_factorial(n):
	z=1
	for i in range(1, n+1):
		z=z*i
	return z


def rec_factorial(n):
	if n >= 1:
		return n*rec_factorial(n-1)
	else:
		return 1

def list_factorial(n):
	z=1
	li= []
	for i in range(1,x+1):
		for j in range(1,i+1):
			z=z*j
		li.append(z)
		z=1
	return li

