n = int(input())

if n % 2 == 0: 
	print("Введите нечетное число")
else : 
	for i in range(1, n, 2): 
		print(" "*(n//2-i//2), "*"*i) 
	for i in range(n, 0, -2): 
		print(" "*(n//2-i//2), "*"*i) 