'''
lambda 
: def와 동일한 역할/ 함수를 한줄로 간결하게 만들때 사용

형식
: lambda 매개변수1, 매개변수2,... : 매개변수를 이요한 표현식
'''
# 합 구하는 def 함수
def sum1(a,b):
    return a+b
print('def :',sum1(3,4))

# 합 구하는 lambda 함수
sum2 = lambda a,b:a+b
print('lambda :',sum2(3,4))

myList = [lambda a,b:a+b, lambda a,b:a*b]

print('myList[0](3,4) :',myList[0](3,4))
print('myList[1](3,4) :',myList[1](3,4))

g = lambda x,y:x+y
print('g(1,2) :',g(3,4))

# 선언하자마자 쓸 수도 있음
print((lambda x:x**x)(3))
# 3**3 = 27

add = lambda x,y:x+y
print('100과 200의 합 :',add(100,200))

# 인라인 람다 함수 
# : 별도의 라인으로 람다함수 정의하지 않고 출문 내에 람다 함수의 기능을 넣을 수 있음
print('100과 200의 합 :',(lambda x,y:x+y)(100,200))

f = lambda *x:max(x)*2
print('f(1,3,7) :',f(1,3,7))

f = [lambda x:x+1, lambda x:x+2, lambda x:x+3]
print('f[0](1) :',f[0](1))
print('f[1](1) :',f[1](1))
print('f[2](1) :',f[2](1))

def sub(x,y):
    return x-y

print('200 - 100 =',sub(200,100))
print('200 - 100 =',(lambda x,y:x-y)(200,100))