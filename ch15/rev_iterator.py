# rev_iterator.py

class ReverseIterator:
    
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration        
        result = self.data[self.position]
        self.position -= 1
        return result
    
ri = ReverseIterator([1, 2, 3, 4, 5])

print(type(ri))
print(next(ri)) # 5

for item in ri: # 4 3 2 1
    print(item)
    
# print(next(ri))   # StopIteration


print(dir(ri))

print('__iter__' in dir(ri))
print('__next__' in dir(ri))