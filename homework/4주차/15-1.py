class MyIterator:
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


it = MyIterator([10, 20, 30])

for value in it:
    print(value)