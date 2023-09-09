def single_letter_count(word, letter):

    return word.lower().count(letter.lower())


print(single_letter_count("Hello World", "h"))
print(single_letter_count("Hello World", "z"))
print(single_letter_count("Hello World", "l"))