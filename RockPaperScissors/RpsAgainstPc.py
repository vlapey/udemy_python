import random

print("...rock...\n...paper...\n...scissors...\n")

rock = "rock"
paper = "paper"
scissors = "scissors"

player_1 = input("enter Player 1's choice\n")
player_1 = player_1.lower()

if player_1 != rock and player_1 != paper and player_1 != scissors:
    print("Enter valid RPS")
    quit()

player_2 = random.randint(1, 3)

if player_2 == 1:
    player_2 = "rock"

elif player_2 == 2:
    player_2 = "paper"

else:
    player_2 = "scissors"

print(player_2)

print("SHOOT!")

if player_1 == player_2:
    print("Tie\n")

elif player_1 == rock and player_2 == scissors:
    print("player_1 won\n")

elif player_1 == paper and player_2 == rock:
    print("player_1 won\n")

elif player_1 == scissors and player_2 == paper:
    print("player_1 won\n")

else:
    print("player_2 won\n")
