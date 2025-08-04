day = int(input("Type a number to see the day: "))

while day !=10:
    match day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case 10:
            break
        case _:
            print("Not a valid number")
    day = int(input("Type a number to see the day: "))
