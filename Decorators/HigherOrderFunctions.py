from random import choice


def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result


def sum(n, func):
    total = 0
    for num in range(1, n + 1):
        total += func(num)
    return total


def square(x):
    return x * x


def cube(x):
    return x * x * x


def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh


print(sum(3, cube))
print(sum(3, square))

print(greet("Toby"))

laugh = make_laugh_func()
print(laugh())