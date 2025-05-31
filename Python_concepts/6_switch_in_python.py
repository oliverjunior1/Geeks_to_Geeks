def switch_case(option):
    switch={
        1:"Option 1",
        2:"Option 2",
        3:"Option 3"
    }
    return switch.get(option, "invalid")

user_option = int(input("Choice a number to 1 to 3:"))
print(switch_case(user_option))