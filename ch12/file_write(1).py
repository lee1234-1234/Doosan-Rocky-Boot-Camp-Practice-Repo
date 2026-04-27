# 파일객체명.write(data)

path = r"ch12\file.txt"
mode = "w"

with open(path, mode, encoding='utf-8') as f:
    f.write("No pain, no gain. \n")
    f.write("노력 없이는 얻는 것도 없다.")