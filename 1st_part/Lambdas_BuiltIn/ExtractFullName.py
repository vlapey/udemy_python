def extract_full_name(some_list):
    return list(map(lambda word: f"{word['first']} {word['last']}", some_list))


print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))
