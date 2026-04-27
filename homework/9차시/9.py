class Phone:
    def __init__(self, company, year, color):
        print("휴대폰 생성")
        self.company = company
        self.year = year
        self.color = color
        
    def info(self):
        print(self.company)
        print(self.year)
        print(self.color)
                
    def setInfo(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color
    
    
my_phone = Phone("삼성전자", 2005, "Blue")
my_phone.info()

my_phone.setInfo("애플", 2025, "Pink")
my_phone.info()