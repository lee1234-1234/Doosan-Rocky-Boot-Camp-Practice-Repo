class Cvalue():
    
    def __init__(self):
        self.lista = []
        
    def add(self, num):
        self.lista.append(num)
        
    def fprint(self):
        print(self.lista)
        
def plus(a, b):
    c = a + b
    return c

# 메인모듈로 실행시, "__main__" 출력
# 하위모듈로 실행시, "모듈명" 출력
if __name__=="__main__":
    print(__name__)
    p1 = Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()