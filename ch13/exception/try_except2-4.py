# try_excepy2.py

print("try_except2-4")

path = r"ch13\exception\myflie1.txt"

try: 
    f = open(path)
    s = f.readline()
    i = int(s.strip())
except (RuntimeError, TypeError, NameError):
    print("RuntimeError, TypeError, NameError 중 하나의 예외 처리!")
except OSError:
    print("OSError")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except ValueError as e:
    print("정수형으로 변환할 수 없습니다.")
    print("e:", e)
except Exception:
    print("Exception")    

print("program exit")