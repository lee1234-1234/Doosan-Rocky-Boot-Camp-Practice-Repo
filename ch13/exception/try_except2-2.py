# try_excepy2.py

print("try_except2")

path = r"ch13\exception\myflie.txt"

try: 
    f = open(path)
    s = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except ValueError:
    print("정수형으로 변환할 수 없습니다.")
    
print("program exit")