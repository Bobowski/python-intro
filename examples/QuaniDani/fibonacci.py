def iter_fibonacci(n):
	j=k=p=1
	print(j)
	for n in range(1,i):
		print(j)
		k=j
		j=j+p
		p=k
		
def rec_fibonacci(n):
	if n == 0 or n == 1:
		return n
	return fibbonaci2(n-1) + fibbonaci2(n-2)
	
def acc_fibonacci(n,a,b):
	if n==0:
		return a
	return acc_fibonacci(n-1,a+b,a)

def list_fibonacci(n):
	lis = []
	j=k=p=1
	lis.append(j)
	for n in range(1,i):
		lis.append(j)
		k=j
		j=j+p
		p=k
	print(lis)
