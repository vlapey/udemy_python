def partition(some_list, fn):
    truthy_list = []
    falsy_list = []
    for element in some_list:
        if fn(element):
            truthy_list.append(element)
        else:
            falsy_list.append(element)
    return [truthy_list, falsy_list]


def isEven(num):
    return num % 2 == 0


print(partition([1, 2, 3, 4], isEven))

