import random
random_number = random.randint(1, 10)
user_input = 0

while True:
    user_input = input("Guess a number between 1 and 10: \n")
    user_input = int(user_input)
    if user_input < random_number:
        print("Too low, try again")
    elif user_input > random_number:
        print("Too high, try again")
    else:
        print("You guessed it!\n")
        choice = input("You wanna try again? (y/n)\n")
        if choice == "y":
            random_number = random.randint(1, 10)
            continue
        else:
            break
