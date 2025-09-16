#Do args with arithmetics operations

def args_sum(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)

args_sum(15,15,15,15,15,15)