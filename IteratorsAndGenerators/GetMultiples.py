def get_multiples(number, count):
    i = 1
    while i <= count * number:
        if i % number == 0:
            yield i
            i += 1
        else:
            i += 1


def get_multiples2(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


def get_unlimited_multiples(number):
    i = 1
    while True:
        if i % number == 0:
            yield i
            i += 1
        else:
            i += 1