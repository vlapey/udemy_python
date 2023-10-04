def multiply_even_numbers(some_list):
    product = 1
    for i in some_list:
        if i % 2 == 0:
            product *= i

    return product


print(multiply_even_numbers([1, 2, 3, 4, 5, 6]))
