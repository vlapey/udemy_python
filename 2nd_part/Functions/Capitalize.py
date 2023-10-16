def capitalize(some_string):
    """returns first letter capitalized of a string
    >>> capitalize('work')
    'Work'
    >>> capitalize(123)
    Traceback (most recent call last):
        ...
    ValueError: some_string must be string
    """

    return some_string[:1].upper() + some_string[1:]


print(capitalize("hello"))
