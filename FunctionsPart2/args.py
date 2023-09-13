def contains_purple(*args):
    if "purple" in args:
        return True
    return False


print(contains_purple("green", False, 37, "blue", "hello world", "purple"))
