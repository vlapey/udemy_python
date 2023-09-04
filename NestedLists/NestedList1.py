board = [[num for num in range(1, 4)] for val in range(1, 4)]
answer = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(answer)