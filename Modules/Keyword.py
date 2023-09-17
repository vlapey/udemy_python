import keyword


def contains_keyword(*args):
    return any(i for i in args if keyword.iskeyword(i))


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
