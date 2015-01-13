def fibo(n):
	if n <= 2:
		return 1
	else:
		return fibo(n - 1) + fibo(n - 2)
		
for i in range(1, 20):
	print fibo(i)