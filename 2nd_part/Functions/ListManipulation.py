def list_manipulation(some_list, command, location, value=None):
    if command == "remove":
        if location == "end":
            return some_list.pop()
        if location == "beginning":
            return some_list.pop(0)
    if command == "add":
        if location == "beginning":
            some_list.insert(0, value)
            return some_list
        if location == "end":
            some_list.append(value)
            return some_list


new_list = list_manipulation([1, 2, 3], "add", "beginning", 30)
print(new_list)
