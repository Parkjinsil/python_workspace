'''
다중 상속시 상속 받을 클래스의 이름이 앞 쪽에 있는 클래스가 우선권을 얻음
즉, 클래스1과 클래스2, 클래스3에 동일한 이름의 메서드가 있다면 클래스1의 메서드를 상속해 옴
'''
class Base1:
    def myfunc(self):
        print("Base1")
        
class Base2:
    def myfunc(self):
        print('Base2')
    member1 = 100
    member2 = 200
    
class Base3:
    def myfunc2(self,a,b):
        print(a+b)

class InhClass(Base1, Base2, Base3):
    member3 = 300
    
ex1 = InhClass()
ex1.myfunc() # Base1
ex1.myfunc2(ex1.member1, ex1.member3) # 400