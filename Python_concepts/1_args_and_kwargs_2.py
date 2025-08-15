#Do args with arithmetics operations

def args_sum(*args):
    sum = 0
    for x in args:
        sum += x
    return print(sum)

args_sum(10,10,10)

