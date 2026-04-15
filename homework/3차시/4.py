# 8번
num = int(input())
numminus = num - 20
if numminus < 0:
    print(0)
elif numminus > 255:
    print(255)
else:
    print(numminus)