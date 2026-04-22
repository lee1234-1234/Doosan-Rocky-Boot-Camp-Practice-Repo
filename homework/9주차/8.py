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
    
    
my_phone = Phone("삼성전자", 2005, "Blue")
my_phone.info()