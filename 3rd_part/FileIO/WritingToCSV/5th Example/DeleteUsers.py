from csv import reader, writer


def remove_users(old_name, old_lastname):
    with open("users.csv") as file:
        rows = list(reader(file))

    with open("users.csv", "w") as file:
        writer_object = writer(file)
        removed_users = 0
        for row in rows:
            if row[0] == old_name and row[1] == old_lastname:
                removed_users += 1
            else:
                writer_object.writerow(row)

        return f"Users removed: {removed_users}."
