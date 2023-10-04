for digit in range(1, 21):
    if digit == 4 or digit == 13:
        print(f"{digit} is unlucky")
    elif digit % 2 == 0:
        print(f"{digit} is even")
    else:
        print(f"{digit} is odd")
