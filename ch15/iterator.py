# iterator.py

class MyIterator:
    # 1. 멤버변수
    # 2. 멤버함수(메서드)
    def __init__(self, data):
        self.data = data
        self.position = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result


i = MyIterator([1, 2, 3])
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

print(type(i))

for item in i:
    print(item)
    

## 이터레이터 사용 목적:
# 데이터를 한번에 다 들고 있지 않고,
# 필요할 때마다 하나씩 꺼내 쓰기 위해
# - 리스트는 모든 값을 메모리에 저장해 사용
# - 이터레이터는 값을 하나씩 생성 => 메모리 거의 안씀