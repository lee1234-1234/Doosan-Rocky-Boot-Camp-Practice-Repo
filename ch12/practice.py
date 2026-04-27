import os

path = r"ch12\file\계좌1.txt"
mode = "w"
encoding = "utf-8"

with open(path, mode, encoding=encoding) as file:
    file.write("김삿갓 597-89-000089\n")
    file.write("이수근 343-64-000064\n")
    file.write("박혁거세 136-97-000097\n")