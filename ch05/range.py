nums = range(10)

print(nums)              # range(0, 10)
print(type(nums))        # range
print(type(list(nums)))  # list
print(list(nums))

print("--------------")
print(range(10))         # range(0, 10)
print(list(range(10)))

print("--------------")
print(range(1, 5))
print(list(range(1, 5)))  # [1, 2, 3, 4]

print("--------------")
print(range(2, 9, 2))
print(list(range(2, 9, 2)))  # [2, 4, 6, 8]

print("--------------")
for num in range(3):
    print('안녕 거북이', num)
    
print("--------------")
num = 0
while num < 3:
    print('안녕 거북이', num)
    num = num + 1