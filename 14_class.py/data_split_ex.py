class Data:
    def __init__(self,data):
        tmp = data.split("|") # "|"를 기준으로 text 분해
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]
        
    def print_age(self):
        print(self.age)
        
    def print_grade(self):
        print('%s님 당신의 점수는 %s입니다.'%(self.name,self.grade))
        
data = Data('홍길동|42|A')

data.print_age() # 42

data.print_grade() # 홍길동님 당신의 점수는 A입니다.