#값 추가하기
lista = [1, 2, 3]
print(lista)
lista.append("append")
print(lista)



print("-------------------------")
listc = []
print(listc)
print(type(listc))

listc.append(300)
print(listc)
listc.append("파이썬")
print(listc)
listc.append(3.7)
print(listc)
listc.append(False)
print(listc)
listc.append([1, True])
print(listc)

print("-------------------------")
subject = ['국어', '수학', '영어', '국사']
print(subject)

subject.append('영어')
print(subject)

subject.remove('영어')
print(subject)

print("-------------------------")
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
print(clovers)

del clovers[1]
print(clovers)

print("HH-------------------------")
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers)
clovers.insert(1, '클로버4')
print(clovers)

print("HHH-------------------------")
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers)
clovers.insert(0, '클로버5')
print(clovers)

print("-------------------------")
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers)
clovers.extend([1, 2, 3])
print(clovers)
clovers.append(555555555)
print(clovers)

