class FourCal2:
    def __init__(self,first,second):
        self.first = first
        self.second = second
        self.__my_secret = 500 # private 변수 : 비공개 변수, 클래스 외부에서 호출 X
        
    def sum(self):
        # self.result 로 안 쓰는 이유는 result 값 저장 안하고 한 번 쓰고 날려버리려고
        # result = self.first + self.second
        return self.__mysum()
    
    # 앞에 언더바 두개 : private -> 비공개 함수 , 클래스 내부에서만 쓸 수 있음
    def __mysum(self):
        result = (self.first + self.second)*2 + self.__my_secret
        return result    
    
a = FourCal2(4,2)

print(a.first) # 4 인스턴스 변수
print(a.second) # 2 인스턴스 변수

print(a.sum()) # 512 메소드 실행, self만 매개변수

# print(a.__mysum()) # 호출 안됨 (비공개 메소드)

'''
파이썬에서 '_'(언더스코어) 용도
-> 네이밍 : 한 모듈 내부에서만 사용하는 private 클래스/함수/변수/메서드를 선언할 때 사용하는 컨벤션
'''

