from csv import reader, writer


def add_user(first_name, last_name):
    with open("users.csv", "a", newline="") as file:
        writer_object = writer(file)
        credentials = [first_name, last_name]
        writer_object.writerow(credentials)


def print_users():
    with open("users.csv", "r", newline="") as file:
        reader_object = reader(file)
        next(reader_object)
        for user in reader_object:
            print(f"{user[0]} {user[1]}")


def find_user(first_name, last_name):
    with open("users.csv") as file:
        reader_object = reader(file)
        for (index, row) in enumerate(reader_object):  # 1, row["Colt", "Steele"]\n
            if first_name == row[0] and last_name == row[1]:
                return index
        return f"{first_name} {last_name} not found."
