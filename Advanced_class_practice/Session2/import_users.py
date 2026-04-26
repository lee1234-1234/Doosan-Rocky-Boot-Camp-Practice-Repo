import csv

def load_users(filename):
    users = []

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            user = {
                "user_id": int(row[0]),
                "name": row[1],
                "phone": row[2]
            }
            users.append(user)

    return users
