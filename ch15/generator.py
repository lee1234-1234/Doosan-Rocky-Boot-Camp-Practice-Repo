# generator.py

def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'
    
g = simple_generator()
print(type(g))

print(next(g))
print(next(g))
print(next(g))

print("---------")
print(dir(g))

print('__iter__' in dir(g))
print('__next__' in dir(g))