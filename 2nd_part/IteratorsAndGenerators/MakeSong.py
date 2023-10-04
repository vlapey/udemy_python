def make_song(count=99, beverage="soda"):
    i = count
    while i >= 0:
        if i == 1:
            yield f"Only 1 bottle of {beverage} left!"
            i -= 1
            continue
        if i == 0:
            yield "No more kombucha!"
            i -= 1
            continue
        yield f"{i} bottles of {beverage} on the wall."
        i -= 1


def make_song2(count=99, beverage="soda"):
    for num in range(count, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"