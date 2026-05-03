# with open("data.txt", "a", encoding="utf-8") as file:
#     file.write("11번째 줄입니다.\n")

# with open("data.txt", "r", encoding="utf-8") as file:
#     contents = file.read()

# print(contents)

with open(r"homework\4주차\data.txt", "a", encoding="utf-8") as file:
    file.write("11번째 줄입니다.\n")

with open(r"homework\4주차\data.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)