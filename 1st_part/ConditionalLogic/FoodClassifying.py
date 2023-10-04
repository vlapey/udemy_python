# NO TOUCHING ============================================
from random import choice
food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])

# YOUR CODE GOES HERE
if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
elif food == "dirt" or food == "worm":
    print("yuck")