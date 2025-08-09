# args and kwargs with four elements

def args_kwargs(*args, **kwargs):
    print(args, kwargs)

args_kwargs(1,2,3,a=1,b=2, c=3)

#Do args with arithmetics operations

def args_with_arithmetics(*args):
    sum = 0
    for x in args:
        sum += x
    return print(sum)

args_with_arithmetics(10,20,30,40,50)