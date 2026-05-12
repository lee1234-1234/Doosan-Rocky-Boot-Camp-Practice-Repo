ca = [21, 10, 11, 15, 13]
mina = ca[0]
minix = 0
for sb in range(1, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb
        
temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp
print(ca)