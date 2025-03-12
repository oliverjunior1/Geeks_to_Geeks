def kwargs_and_args(*args, **kwargs):
    print(f"The args are: {args} and the kwargs are {kwargs}.")

kwargs_and_args(1,2,3, a=4, b=5, c=6)