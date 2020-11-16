a = True
while a:
    number = input("age:")
    if not number:
        print("ok!")
    elif int(number) == 16:
        print("???")
        a = False
    elif int(number) < 16:
        print("yes")
    elif int(number) > 16:
        print("no")
