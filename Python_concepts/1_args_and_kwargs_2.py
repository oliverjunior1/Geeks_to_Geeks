#Do args with arithmetics operations

def args_sum(*args):
    sum =0
    for arg in args:
        sum -= arg
    print(sum)

args_sum(1,2,3,4,5)