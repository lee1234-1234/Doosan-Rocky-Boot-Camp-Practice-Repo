# try_excepy2.py

print("try_except2")

path = r"ch13\exception\myflie.txt"
# FileNotFoundError -> 실제로 파일이 없거나 / w 모드가 아닌 r 모드를 사용해서 에러

f = open(path)          # 기본 'r'모드
# f = open(path, "w")          

# io.UnsupportedOperation
s = f.readline()

# ValueError
i = int(s.strip())
        
print("program exit")