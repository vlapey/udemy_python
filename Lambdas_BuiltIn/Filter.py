def remove_negatives(some_list):
    return list(filter(lambda num: num >= 0, some_list))


print(remove_negatives([50,60,70]))
