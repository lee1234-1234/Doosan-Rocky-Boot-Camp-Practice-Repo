sta = "python example"
lena = len(sta)
print(lena)

print("-------------------")
def string_length(stb):
    count = 0
    for i in stb:
        count += 1
    return count
    
lena = string_length(sta)
print(lena)