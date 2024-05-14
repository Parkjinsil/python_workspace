class Calculator: 
    def __init__(self): # 초기자
        self.result = 0
        
    def add(self,num): # 메서드
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3)) # 3
print(cal1.add(4)) # 7
print(cal2.add(3)) # 3
print(cal2.add(7)) # 10