class Calculator:
    def __init__(self,data):
        self.data = data
        
    def sum(self):
        result = sum(self.data)
        return result
    
    def avg(self):
        length = len(self.data)
        return self.sum()/length
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum()) 
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())