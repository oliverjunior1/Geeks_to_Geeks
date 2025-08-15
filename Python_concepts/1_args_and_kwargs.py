# args and kwargs with four elements

def args_and_kwargs(*args, **kwargs):
    print(f"args:{args}, kwargs:{kwargs}")


args_and_kwargs(1,2,3,4, a=1,b=2, c=3, d=4)


