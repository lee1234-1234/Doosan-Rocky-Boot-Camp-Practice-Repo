class MyRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result
    
    
    
for i in MyRange(1, 10, 2):
    print(i)
    
    
it = MyRange(1, 10, 2)

print(next(it))
print(next(it))
print(next(it))
print(next(it))