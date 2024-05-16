class FourCal:
    # 클래스 변수 (클래스 공통변수, 인스턴스에 독립적이지 않음)
    COUNT = 0
    
    # 클래스 내의 함수는 메소드라고 부름
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def sum(self):
        result = self.first + self.second
        FourCal.COUNT += 1
        return result
    
a = FourCal() # 인스턴스 생성
a.setdata(4,2) # 인스턴스 메소드 실행
print(a.first) # 4
print(a.second) # 2

# FourCal.setdata(a,7,8) # 클래스 메소드로 실행
# print(a.first) # 7
# print(a.second) # 8

'''
"클래스명.메서드(FourCal.setdata())" 형태로 호출할 때는 객체 a를 입력 인수로 꼭 넣어줘야 함
반면에 "객체.메서드(a.setdata())" 형태로 호출할 때는 첫 번째 입력 인수(self)를 반드시 생략해야 함
'''

b = FourCal()
print(a.sum()) # 6

# 클래스 변수는 클래스명.변수로 써야함 (인스턴스 객체 말고)
print(FourCal.COUNT) # 1

b.setdata(7,8)
print(b.sum()) # 15

print(FourCal.COUNT) # 2

print(a.sum())

print(FourCal.COUNT) # 3

b.sum()

print(FourCal.COUNT) # 4







