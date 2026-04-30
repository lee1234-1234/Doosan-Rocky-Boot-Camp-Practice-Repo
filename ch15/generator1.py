# generator1.py

def mygen():
    for i in range(1, 100):
        result = i * i * i * i * i
        yield result
        
gen = mygen()
print(gen)

for item in gen:
    print(item)