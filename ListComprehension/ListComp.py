answer = [name[0] for name in ["Elie", "Tim", "Matt"]]
print(answer)
answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(answer2)
with_vowels = "This is so much fun"
without_vowels = "".join(char for char in with_vowels if char not in "aoeiu")
print(without_vowels)
# how join itself works
cooldude = ' '.join(["cool", "dude"])
print(cooldude)