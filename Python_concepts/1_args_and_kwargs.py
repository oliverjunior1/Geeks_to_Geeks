def kwargs_args(*args, **kwargs):
    print(args, kwargs)
while True:
    x = dict(input("Put the dates: "))
    print(kwargs_args(x))
