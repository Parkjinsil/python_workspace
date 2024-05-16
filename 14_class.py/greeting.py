class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
        
class B(A):
    # def greeting(self):
    #     print('안녕하세요. B입니다.')
    pass
        
class C(A):
    # def greeting(self):
    #     print('안녕하세요. C입니다.')
    pass
        
class D(B,C):
    pass

x = D()
x.greeting() # 안녕하세요. A입니다.
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]


