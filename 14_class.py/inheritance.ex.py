'''
상속 : Inheritance
-> 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
'''
class FourCal:
    def __init__(self,first, second):
        self.first = first
        self.second = second
        self.__third = 10 # 자식도 접근 X
    def sum(self):
        print(self.__mysum()) # 호출 O
        result = self.first + self.second
        return result 
    def __mysum(self): # 자식도 접근 X
        result = 2*(self.first + self.second)
        return result
     
class MoreCal(FourCal): # FourCal거 상속
    def pow(self):
        result = self.first**self.second
        return result
    
m = MoreCal(4,2)
print(m.pow()) # 16

print(m.sum()) # 6
# print(m.__mysum()) # 호출 안됨
