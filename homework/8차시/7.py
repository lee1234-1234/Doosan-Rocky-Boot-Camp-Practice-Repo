su = [8, 10, 11, 24, 1, 25, 54]

def fmax(fu):
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su)
print("최대값 max는", max)