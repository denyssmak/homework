a = int(input())
l1 = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in l1: 
	if a // i:
		print(a // i, i)  
		a = a - (a // i)*i