# with open("data.txt", "w", encoding="utf-8") as file:
#     for i in range(1, 11):
#         file.write(f"{i}번째 줄입니다.\n")

# print("파일이 성공적으로 작성되었습니다.")

# with open("data.txt", "r", encoding="utf-8") as file:
#     contents = file.read()

# print("파일내용:")
# print(contents)

with open(r"homework\4주차\data.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11):
        file.write(f"{i}번째 줄입니다.\n")

print("파일이 성공적으로 작성되었습니다.")

with open(r"homework\4주차\data.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print("파일내용:")
print(contents)