# decorations without method
def fun(x):
    def fun2():
        print("###################")
        x()
        print("###################")
    return fun2

@fun
def greetings():
    print("Hello Joaquim")

greetings()