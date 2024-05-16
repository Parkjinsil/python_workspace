'''
만약 같은 이름의 멤버변수나 멤버함수가 부모, 자식 클래스에 공통으로 있다면 자식클래스의 것으로 덮어쓰기 됨
'''
class BaseClass:
    def myfunc(self):
        print("BaseClass's myfunc")
        
class InhClass(BaseClass):
    def myfunc(self):
        print("InhClass's myfunc")
        
ex1 = BaseClass()
ex1.myfunc() # BaseClass's myfunc
ex2 = InhClass()
ex2.myfunc() # InhClass's myfunc

