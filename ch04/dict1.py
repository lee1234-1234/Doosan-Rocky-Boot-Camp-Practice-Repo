my_dict1 = {}
print(my_dict1)
print(type(my_dict1))

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2)

my_dict3 = {'이름': '엘리스', '나이' : 10, '시력' : [1.0, 1.2]}
print(my_dict3)

print(my_dict3['이름'])
print(my_dict3['나이'])
print(my_dict3['시력'])

print(my_dict3.get('이름'))

my_dict3['키'] = '175cm'
print(my_dict3)

my_dict3['나이'] = 11
print(my_dict3)

print("-------------------------")
clover = {'나이':27, '직업':'병사'}
print(clover)

clover['번호'] = 9
print(clover)

clover['번호'] = 8
print(clover)

clover1 = {'나이':37, '직업':'마법사', '능력':{'체력1':70, '마력':30}}
print(clover1)

print("-------------------------")

me = {'이름': '홍길동', '나이': 72, '성별':'남자', '키':165}
me['전화번호'] = '010-0000-1111'
me['주소'] = '구로'
print(me)
print(me.get('이름'))

print(me.items())
print(me.keys())
print(me.values())