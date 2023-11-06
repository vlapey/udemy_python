from csv import reader, writer


def update_users(old_name, old_lastname, name, lastname):
    with open("users.csv") as file:
        rows = list(reader(file))

    with open("users.csv", "w") as file:
        writer_object = writer(file)
        updated_users = 0
        for row in rows:
            if row[0] == old_name and row[1] == old_lastname:
                writer_object.writerow([name, lastname])
                updated_users += 1
            else:
                writer_object.writerow(row)

        return f"Users updated: {updated_users}."


print(update_users("Colt", "Steele", "Hallberg", "Anderson"))
