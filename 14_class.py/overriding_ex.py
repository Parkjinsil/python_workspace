'''
메서드 오버라이딩(Overriding, 덮어쓰기)
: 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
  super().메서드 이름을 사용해 부모 클래스의 메서드를 호출할 수 있음
'''
class Person:
    def greeting(self):
        print('안녕하세요')
    
class Student(Person):
    def greeting(self):
        super().greeting() # 부모 클래스의 메서드 호출
        print('저는 파이썬 코딩 학생입니다.') # 추가 메서드
        
tom = Person() 

tom.greeting() # 안녕하세요

james = Student()

james.greeting()
# 안녕하세요
# 저는 파이썬 코딩 학생입니다.