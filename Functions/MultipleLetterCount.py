#multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}


def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in set(word)}


print(multiple_letter_count("awesome"))
