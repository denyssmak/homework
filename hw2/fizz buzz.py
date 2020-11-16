fizz = int(input())
buzz = int(input())
jezz = int(input())

for x in range(1, jezz+1):
    if (x % fizz == 0) and (x % buzz == 0):
        print('F', end=" ")
    elif x % buzz == 0:
        print('B', end=" ")
    elif x % fizz == 0: 
        print('FB', end=" ")
    else:
        print(x, end=" ") 
    

