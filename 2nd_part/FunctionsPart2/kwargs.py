def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(vlad="blue", colt="purple")


def combine_word(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    if "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


print(combine_word("child", prefix="man"))
