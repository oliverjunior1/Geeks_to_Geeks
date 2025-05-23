# args and kwargs with five elements

def args_and_kwargs(*args, **kwargs):
    print(args, kwargs)

args_and_kwargs(1,2,3,4,5, a=1, b=2, c=3, d=4, e=5)
