#Do args with arithmetics operations

def args_and_kwargs(*args, **kwargs):
    sum = 0
    for x in args:
        sum += x
    return sum

print(args_and_kwargs(10,20,3,4,50))