from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any([num for num in args if type(num) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)

    return wrapper


@only_ints
def add(x, y):
    return x + y


print(add(4, 3))