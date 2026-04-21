ca = [21, 10, 11, 15, 13]
print(ca)

for sa in range(len(ca) - 1):
    mina = ca[sa]
    minix = sa

    for sb in range(sa + 1, len(ca)):
        if mina > ca[sb]:
            mina = ca[sb]
            minix = sb

    temp = ca[sa]
    ca[sa] = ca[minix]
    ca[minix] = temp
    print(ca)