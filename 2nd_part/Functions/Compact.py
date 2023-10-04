def compact(some_list):
    return [i for i in some_list if i]


print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))

