# 10. 주어진 딕셔너리에서 모든 값의 합을 구하는 함수를 작성하세요. 
# ( 예를 들어, 딕셔너리 { 'a': 10, 'b': 20, 'c': 30 }가 주어졌을 때, 합은 60 )

def sum_dic(a):
    total = 0
    for value in a.values():
        total += value
    return total

data = {'a': 10, 'b': 20, 'c': 30}
print(sum_dic(data))