def is_all_strings(some_list):
    return all(type(word) is str for word in some_list)


print(is_all_strings(['hello', 'goodbye']))
