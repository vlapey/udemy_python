from functools import wraps
from time import sleep


def delay(time):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {time}s before running {fn.__name__}")
            sleep(time)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    return "hi"


print(say_hi())
