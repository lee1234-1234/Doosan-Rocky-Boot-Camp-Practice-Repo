clovers = ('클로버1', '클로버2', '클로버3')
print(clovers[1])

print(clovers)
print(type(clovers))

my_tuple = ()
print(my_tuple)
print(type(clovers))

print("---------------------")
my_tuple1 = ()
print(my_tuple)
print(type(my_tuple))

my_tuple2 = (1, -2, 3.14, True, "hi", [1, 2])
print(my_tuple2)
print(type(my_tuple))

my_tuple3 = 1, -2, 3.14, True, "hi", [1, 2]
print(my_tuple3)
print(type(my_tuple3))

print("---------------------")
my_int = (1)
print(type(my_int))
my_int = (1, )
print(type(my_int))

print("---------------------")
my_list3 = list(my_tuple3)
print(my_list3)
print(type(my_list3))
my_list3[3] = False
print(my_list3)