na = 10
nb = 11
print("na 값:", na, end=" ")
print("nb 값:", nb)

temp = na
na = nb
nb = temp
print("na 값:", na, end=" ")
print("nb 값:", nb)

print('-----------')
na = 10
nb = 11
print("na 값:", na, end=" ")
print("nb 값:", nb)

na, nb = nb, na
print("na 값:", na, end=" ")
print("nb 값:", nb)