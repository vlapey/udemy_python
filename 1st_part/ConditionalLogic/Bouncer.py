try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("Enter valid int number")
    quit()

if age:
    if 18 <= age <= 21:
        print("18-21 Wristband")
    elif age > 21:
        print("21+ drink, normal entry")
    else:
        print("Too young, sry")

else:
    print("Please enter your age")
