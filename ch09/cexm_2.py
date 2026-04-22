class Cexm:
    def fsam(self):
        print("멤버 함수(메서드)")
    
    def fsbm(self, pa):
        self.x = pa
        print("멤버 변수 X는", self.x)
        
ca = Cexm()
ca.fsam()
ca.fsbm(10)

cb = Cexm()
cb.fsam()
cb.fsbm(20)