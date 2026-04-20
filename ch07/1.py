def funca(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    return pa, pb
    
na = 10
nb = 11
print("na 값은 ", na, "nb 값은 ", nb)
funca(na, nb)
print("na 값은 ", na, "nb 값은 ", nb)