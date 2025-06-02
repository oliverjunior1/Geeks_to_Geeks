# args and kwargs with five elements

def args_and_kwargs(*args, **kwargs):
    print(args, kwargs)

args_and_kwargs(1,2,3,4,5, num=1, num1=2, num2=3, num3=4, num4=5)

