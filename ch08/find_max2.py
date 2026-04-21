su = [5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    return max


# a = su[0]
# b = su[1]
# c = su[2]
# d = su[3]
# e = su[4]

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최대값:", max)

print("3---------------------")
def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최대값:", max)


print("4---------------------")
def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최대값:", max)


print("5---------------------")
def fmax(a, b, c, d, e):
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최대값:", max)

print("6---------------------")
def fmax(fu):
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su)
print("최대값 max는", max)

print("7---------------------")
def fmax(fu):
    max = fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

fu = su
max = fmax(su)
print("최대값 max는", max)


print("8---------------------")
# su = [5, 4, 7, 10, 6]
def fmax(fu):
    max = fu[0]
    for i in range(1, len(fu), 1):
        if max < fu[i]:
            max = fu[i]
    return max

su = [5, 4, 3, 5, 6, 14, 24, 25, 26]
max = fmax(su)
print("최대값 max는", max)