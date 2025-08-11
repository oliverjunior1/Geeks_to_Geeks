#Do args with arithmetics operations

def args_and_kwargs(*args, **kwargs):
    sum = 0
    sum2 = 0
    for x in args:
        sum += x
    return sum

print(args_and_kwargs(50,50,50,50, a=20, b=50))