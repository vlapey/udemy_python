def interleave(first_string, second_string):
    return ''.join((''.join(x) for x in zip(first_string, second_string)))


print(interleave('lzr','iad'))