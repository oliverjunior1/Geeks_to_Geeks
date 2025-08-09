#Do args with arithmetics operations

def args_with_arithmetics(*args):
    sum = 0
    for x in args:
        sum += x
    return print(sum)

args_with_arithmetics(10,20,30,40,50)