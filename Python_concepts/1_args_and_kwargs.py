# args and kwargs with four elements
#
# def args_and_kwargs(*args, **kwargs):
#     print(args, kwargs)
#
# args_and_kwargs(1,2,3, a= 1, b=2)

# Do args with arithmetics operations
def args_args(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(args_args(10,10,10))