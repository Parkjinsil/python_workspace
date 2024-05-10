'''
function(함수)
: 해결해야 하는 문제들의 범위가 커지고 복잡해지면 그 문제를 해결하기 위해 작성해야 하는 프로그램도 커짐
  전체 프로그램을 작고 간단한 프로그램으로 나누어서 작업하면 문제 해결 가능
  이런 작고 간단한 프로그램들 = 함수
  전체 프로그램 = 함수의 합
  
def func_name(x1, x2, ...)
    code1
    code2
    ...
    return n1[,n2,...]

매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 "변수" 
인자 (arguments) : 함수를 호출될 때 전달되는 실제 값 (= 인수, 전달인자)
ex) 위 함수에서 x1, x2 -> 매개변수
       실제로 func_name(2, 3)  -> 2, 3 은 인수

return문을 만나면 함수를 바로 빠져나감 -> 함수를 빠져나가고자 할 때 return을 단독으로 써서 나갈 수 있음
return문 없어도됨

* 함수 안에서 정의된 변수 : 지역변수 
                          함수 내에서 정의되었다가 함수 끝나면 사라짐
                          메인함수에 영향 X
'''

# 두 값의 합을 반환하는 get_sum() 함수
def get_sum(a,b):
    return a+b

n1 = get_sum(10, 20)
print('10과 20의 합 =',n1)

def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result)
# 결과값이 2개인데 변수는 result 하나만 썼는데 오류가 날까? X
# 함수의 결과값은 언제나 1개라서 튜플값으로 패킹해준다.
# 만약에 2개의 결과값으로 받고 싶다면 이렇게 써라
sum, mul = sum_and_mul(3, 4)
print(sum, mul)

# 근의 공식 구하기
def get_root(a,b,c):
    x1 = (-b +(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b -(b**2-4*a*c)**0.5)/(2*a)
    return (x1, x2)

try:
    result1, result2 = get_root(1, 2, -8)
except: # 오류처리
    print('0으로 나누어서 근을 구할 수 없습니다.')
else:   # 정상처리
    print(result1, result2)
    
# 디폴트값 : 전체 변수에 모두 할당하거나 뒤에 있는 매개변수부터 할당해야 함
def div (a, b=2):
    return a/b

print('div(4) :',div(4))

def print_sub(a,b):
    '''
    이 함수는 a,b의 차이를 구하는 함수입니다.
    '''
    # 이렇게 함수 안에 주석으로 써 놓으면 함수에 마우스를 올렸을 때 설명이 뜸
    return '%d과 %d의 차는 %d입니다.'%(a,b,a-b)

print(print_sub(10,20))

def print_multi(a,b):
    return '%d과 %d의 곱은 %d입니다.'%(a,b,a*b)

print(print_multi(10,20))

'''
 가변인자 args : 인자의 수가 정해지지 않음 (Tuple) / 이런게 있다 정도만
 -> 매개변수 앞에 (*) 표시
    그러면 입력값들을 전부 모아서 "튜플"로 만들어 줌 : 꺼내쓸 수 있다는 뜻
'''

def greet(*names):
    for name in names:
        print('안녕하세요',name,'씨')
print(greet('홍길동','양만춘','이순신')) # 인자가 3개
print(greet('James','Thomas')) # 인자가 2개

def sum_mul(choice, *args):
    if choice=='sum':
        result=0
        for arg in args:
            result +=arg
    elif choice=='mul':
        result=1
        for arg in args:
            result *=arg
    return result
print(sum_mul('sum', 1,2,3,4,5))
print(sum_mul('mul',1,2,3,4,5))

def sum_nums(*nums):
    print('3 개의 인자',nums)
    sum=0
    for num in nums:
        sum+=num
    return '합계 : %d , 평균 : %d'%(sum,sum/len(nums))
print(sum_nums(10, 20, 30))
print(sum_nums(10, 20, 30, 40, 50))

def min_nums(*nums):
    return '최솟값은 %d'%min(nums)
print(min_nums(20, 40, 50, 10))

'''
키워드 파라미터 kwargs (keyword arguments) / 이런게 있다 정도만
-> 딕셔너리 변수 (Dictionary)
   매개변수 앞에 (**) 표시
   인수로 key=value 형태를 주었을 때 입력 값 전체가 kwargs라는 "딕셔너리"에 저장됨
'''

def func(**kwargs):
    print(kwargs)
    
print(func(a=1)) # {'a': 1}
print(func(name='foo',age=3)) # {'name': 'foo', 'age': 3}

def func(*args, **kwargs):
    print(args)
    print(kwargs)

# (1, 2, 3)
# {'name': 'foo', 'age': 3}    
print(func(1,2,3,name="foo",age=3))

'''
전역변수
: 함수 바깥에서 선언되거나 전체 영역에서 사용 가능한 변수
: 웬만하면 전역변수 사용 X (옛날에나 많이 씀), 로컬변수 사용 O
-> 요즘에는 class 에 static 변수로 많이 씀
: 굳이 쓰고 싶다면 변수명을 대문자로 해서 전역변수인지 알 수 있게 해라
'''

# 전역 변수
a = 10 
b = 20 

def print_sum():
    # 지역 변수(로컬 변수)
    a = 100
    b = 200
    print('내부 id(a) :',id(a)) # 140722823308824
    print('print_sum() 내부:',a,'과',b,'의 합은',a+b) # 300 (로컬 변수)
    
print_sum()
print('외부 id(a) :',id(a)) # 140722823305944
print('print_sum() 내부:',a,'과',b,'의 합은',a+b) # 30 (지역 변수)

# global : 함수 밖 변수를 사용하겠다는 뜻 -> 추천 X
def print_sum():
    global a,b  # a,b는 함수외부에서 선언된 a,b를 사용함
    a = 100
    b = 200
    result = a+b
    print('print_sum()내부:',a,'과',b,'의 합은',result,'입니다.') # 300
    
a = 10
b = 20
print_sum()
result = a+b
print('print_sum()외부:',a,'과',b,'의 합은',result,'입니다.') # 300
    
# 내장 함수
# abs(x) : 절대값 반환
print(abs(-3)) 

# print(help(dict())) # 함수설명

# sorted(iterable)
dic = {82:"한국", 1:'미국', 81:'일본', 44:'영국'}
print(sorted(dic.items(), reverse=True)) # key 정렬
print(sorted(dic.items(), key=lambda x:x[1])) # value 정렬

# slice(start,end,step, reverse=True)
lst =[0,1,2,3]
print('lst[0:2] :',lst[0:2])
print(lst[slice(0,2)])

# eval() : 문자열을 수식화해서 평가한 다음 값 반환
print(eval('2+3')) # 5

# filter(function, iterable) -> 실제 값 확인하려면 다시 리스트나 다른 iterable로 명시적으로 변환해야함
a = [1,2,3,4]
print(list(filter(lambda x:x%2==0,a)))

# divmod(x,y) : x/y의 몫과 나머지를 tuple로 반환
# pow(x,y) : x**Y 반환

'''
형변환 함수
- int(x)
- float(x)
- str(x)
- list(seq)  -> sequence 순서형 데이터 
- tuple(seq)
'''

print(list('happy'))  # ['h', 'a', 'p', 'p', 'y']
print(tuple('happy')) # ('h', 'a', 'p', 'p', 'y')

# input() : 사용자로부터 데이터를 입력받는 함수

# type() : 객체의 자료형 반환
print(type(123)) # int
print(type('Hello String!')) # str
print(type(120.3)) # float
print(type([100,300,600])) # list

'''
모듈
: 이미 작성해 놓은 프로그램

import 모듈명
-> 모듈명.함수명()
-> 그 모듈의 다양한 함수를 쓰려면 이렇게

from 모듈명 import 함수명
-> 함수명()
-> 이 특정 함수만 여러번 쓸거면 이렇게
'''

'''
모듈 : 파이썬 코드를 논리적인 단위로 구조화하여 작성한 "파일"
       변수,함수,클래스 등을 포함할 수 있음
       import로 가져와서 씀

라이브러리 : 특정 기능을 수행하기 위해 미리 작성된 "모듈들의 집합"
            여러 모듈로 구성되어 있음
            
ex) Python 표준 라이브러리 > math 모듈, os 모듈, re 모듈 등이 포함되어있음
    외부 라이브러리 : NumPy, Pandas, Matplotlib 등이 있음
'''

from datetime import datetime
# yyyy-mm-dd HH24:mm
year = datetime.now().year
month = datetime.now().month
date = datetime.now().day
hour = datetime.now().hour
minute = datetime.now().minute
print('now :',str(year),'-',str(month),'-',str(date),',',str(hour),':',str(minute))

'''
함수 vs 메소드

'''

def is_odd(x):
    '''
    x가 홀수이면 True 리턴, 짝수이면 False 리턴
    '''
    if x%2==1:
        return True
    else :
        return False
print(is_odd(3))

# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수 작성(단, 입력으로 들어오는 수의 개수는 정해져 있지 않음)
def aver(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum/len(nums)
print(aver(2,4,6))

# 구구단 출력
def dan(n):
    for i in range(1,10):
        print('%d x %d = %d'%(n,i,n*i))
        
n = int(input('자연수를 입력하시오(2부터 9까지) :'))
dan(n)



