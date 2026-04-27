with open("./pizza_file1.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")