#Функция которая будет простое число возводить в кладрат через map

n = int(input())
s = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)] for i in sub] ]

print(*s )
def square(a):
    return a ** 2  
print(list(map(square, s)))