while True:
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    c = int(input("Type another different number or 00 to exit: "))
    if c==00:
        break
    else:
        x = lambda a,b,c: (a**b)//c

        print(x(a,b,c))


