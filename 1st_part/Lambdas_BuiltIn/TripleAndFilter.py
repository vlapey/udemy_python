def triple_and_filter(some_list):
    return list(map(lambda num: num * 3, filter(lambda num: num % 4 == 0, some_list)))


print(triple_and_filter([6,8,10,12]))