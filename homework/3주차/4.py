numbers = [42, 17, 23, 56, 9, 34]

min_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num

print(min_val)