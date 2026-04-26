import csv

def load_books(filename):
    books = []

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            book = {
                "book_id": int(row[0]),
                "title": row[1],
                "author": row[2],
                "available": row[3] == "True"
            }
            books.append(book)
    return books