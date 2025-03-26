def argsKwargs(*args, **kwargs):
    return print(f"args: {args}, kwargs: {kwargs}")

argsKwargs(10,20,30,40,a=50, b=60, c=70, d=80)
