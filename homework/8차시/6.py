a = [3, 6, 7, 4, 9, 10, 13]

for i in range(len(a)):
    if a[i] % 2 == 0:
        even_idx = i
        break

for i in range(len(a)-1, -1, -1):
    if a[i] % 2 == 1:
        odd_idx = i
        break

a[even_idx], a[odd_idx] = a[odd_idx], a[even_idx]

print(a)