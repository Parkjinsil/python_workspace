'''
filter()
: iterable의 각 항목에 대해 특정 조건을 적용하여 그 조건을 만족하는 항목들만 남기는 데 사용
: iterable에서 함수의 조건을 만족하는 항목들만 모아서 filter 객체 반환

형태
filter(함수, iterable)
-> 함수 : iterable의 각 항목을 평가하여 True / False 반환
          (파이썬에서는 양수-> True
                       음수, 0 -> False)

'''

f = lambda x:x>0
print(list(filter(f, range(-5,5)))) # [1,2,3,4]

a=range(1,11)
print(list(filter(lambda x:x%2==1,a))) # [1,3,5,7,9]
print([x for x in range(1,11) if x%2==1]) # [1,3,5,7,9]

# lambda x:x%2==1
# -> 표현식에 조건식이 온 람다함수
#    이 경우 조건식이 만족하면 True, 아니면 False 반환

lst = ["서울시 강남구 대치동",
        "서울시 서대문구 북가좌2동",
        "충청남도 당진군 신평면", 
        "대전광역시 유성구 궁동"]
print(list(filter(lambda x:x.find('서울시')!=-1, lst)))

# find() => 특정부분 문자열이 처음으로 나타나는 인덱스 반환 / 없으면 -1

def func(x):
    if x>0:
        return x
    else:
        return x-100
    
print('여기',list(filter(func,range(-5,5))))

'''
0 -> False
양수, 음수 -> True
'''

def minus_func(n): # n이 음수면 True, 아니면 False
    if n<0:
        return True
    else :
        return False
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = [] # 음수를 저장할 리스트
for n in filter(minus_func, n_list):minus_list.append(n)
print('음수 리스트 :',minus_list)

minus_list1 = []
for n in filter(lambda x : x<0, n_list):
    minus_list1.append(n)
print('lambda) 음수 리스트 :',minus_list1)

n_list = [1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda x:x%2==0,n_list))
print(even_list)

odd_list = list(filter(lambda x:x%2==1,n_list))
print(odd_list)

a = [1,2,3,4,5,6,7]
square_a=[]
for n in a:
    square_a.append(n**2) # n의 제곱을 square_a 리스트에 추가
print(square_a)

'''
map(적용시킬_함수, iterable, ...)
'''

def square(x):
    return x**2

square_a = list(map(square, a))
print(square_a)

square_a = list(map(lambda x:x**2, a))
print(square_a)

'''
* map과 filter함수의 차이
: map()은 모든 항목에 함수를 적용하지만, 
  filter()은 조건(함수의 반환값이 True)을 만족하는 항목만 남김
: map()은 기존 항목을 변환하는 반면, filter()은 필터링만 수행(값 변경X)

'''

a_list = ['a','b','c','d']
# def to_upper(x):
#     return x.upper()
    
# upper_a_list = list(map(to_upper,a_list))
# print(upper_a_list)

# upper_a_list = list(map(lambda x: x.upper(), a_list))
# print(upper_a_list)

n_list = [10, 20, 30]
def twice(x):
    return x*2

def triple(x):
    return x*3

n_list2 = list(map(twice,n_list))
print('입력 값의 두 배 :',n_list2)

n_list3 = list(map(triple,n_list))
print('입력 값의 세 배 :',n_list3)

print('입력 값의 두 배 :',list(map(lambda x:x*2,n_list)))
print('입력 값의 세 배 :',list(map(lambda x:x*3,n_list)))

# zip 함수 : 길이가 같은 iterator를 하나로 묶어 반환하는 함수
#            주로, 서로 다른 자료형을 하나의 변수로 묶어서 사용
#            list, set등으로 감싸줘야함
a = "YUN"
b = [1,2,3]
c = ("하나", "둘", '셋')

print(list(zip(a,b,c))) # [('Y', 1, '하나'), ('U', 2, '둘'), ('N', 3, '셋')]
print(set(zip(a,b,c)))  # {('N', 3, '셋'), ('U', 2, '둘'), ('Y', 1, '하나')}
print(dict(zip(a,b)))   # {'Y': 1, 'U': 2, 'N': 3}

L1 = ['A','B','C','D']
L2 = ['가','나','다','라']

# 다중 반복문을 사용하지 않고 하나의 반복문으로 간소화 할 수 있음
for i,j in zip(L1,L2):
    print(i,j)
    
numbers=[[1,2,3],[4,5,6]]

# iterator에 별표(*)를 함께 사용하면 언패킹됨
print(*numbers) # [1, 2, 3] [4, 5, 6]

print(list(zip(*numbers))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6]))) # [(1, 4), (2, 5), (3, 6)]

'''
reduce() 함수 : 각 요소를 누적해 나가는 역할

reduce(함수, iterator)
1. 첫 번째 두 개의 요소를 가지고 함수 적용
2. 그 결과값과 세 번째 요소를 가지고 함수 적용
3. 이대로 순차적으로 하나의 최종 값이 나올 때까지 반복

* 많이 사용되지는 않지만, 리스트나 시퀀스 데이터를 단일 값으로 축약할 때 유용
  ex) 모든 요소를 곱하거나, 최대/최소값을 찾는 등의 작업
* 모듈 functool 임포트 해야함
'''

from functools import reduce
a = [1,2,3,4]
n = reduce(lambda x,y:x+y, a)
print(n) 
# (((1+2)+3)+4) = 10

sum100 = reduce(lambda x,y:x+y,range(1,101))
print('1에서 100까지의 합 :',sum100)

sum10 = reduce(lambda x,y:x*y,range(1,11))
print('10! =',sum10)

# Comprehension(축약형)
L1 = [i**2 for i in range(10) if(i>5)] # [36, 49, 64, 81]
print(L1)

# 셋 다 동일 -> [1, 4, 9, 16, 25, 36, 49] 출력
a = [1,2,3,4,5,6,7]
a1 = list(map(lambda x:x**2, a))
print(a1)

a1 = [x**2 for x in a]
print(a1)

a1 = [x**2 for x in range(1,8)]
print(a1)

st = 'Hello World'
s_list = [x.upper() for x in st]
print(s_list) # ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
print(''.join(s_list)) # HELLO WORLD

data = [0,7,6,9,2,3]
T = tuple((i for i in data))
print(T) # (0, 7, 6, 9, 2, 3)

text = 'YUNDAEHEE'
S1 = set([i for i in text])
print(S1) # {'H', 'N', 'A', 'E', 'Y', 'U', 'D'}
          # set은 중복되는거 없어짐 
          
S2 = {i for i in text} 
print(S2) # {'D', 'U', 'E', 'A', 'Y', 'H', 'N'}

text = 'cheese'
D = {i : text.count(i) for i in text}
print(D) # {'c': 1, 'h': 1, 'e': 3, 's': 1}

cubic = [i**3 for i in range(1,11)]
print(cubic) # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

a = ['welcome','to','the','python','world']
first_a = [x[0] for x in a]
print(first_a) # ['w', 't', 't', 'p', 'w']

ages = [34,39,20,18,13,54]
adult_ages=list(filter(lambda x:x>=19,ages))
print('성년 리스트 :',adult_ages) # 성년 리스트 : [34, 39, 20, 54]
print('성년 리스트 :',[x for x in ages if x>=19])

# 19세보다 적으면 음수로 표시하고 19세보다 크거나 같으면 양수로 표시한 리스트
print([x if x>=19 else -x for x in ages]) # [34, 39, 20, -18, -13, 54]
# 이렇게 if를 "앞"에다 쓰면 if-else 쓸 수 있음

n_list = [-30,45,-5,-90,20,53,77,-36]
minus_list = list(filter(lambda x:x<0,n_list))
print('음수 리스트 :',minus_list) # 음수 리스트 : [-30, -5, -90, -36]
print('음수 리스트 :',[x for x in n_list if x<0])

# s = input('정수 5개를 입력하세요 :').split()
# lst = [int(x) for x in s]
# print(lst)

product_xy = []
for x in [1,2,3]:
    for y in [2,4,6]:
        product_xy.append(x*y)
print(product_xy) # [2, 4, 6, 4, 8, 12, 6, 12, 18]
product_xy = [x*y for x in [1,2,3] for y in [2,4,6]]
print(product_xy)

# 리스트의 축약 표현을 사용한 2와 3의 배수 구하기
print([n for n in range(1,31) if n%2==0 if n%3==0]) # [6, 12, 18, 24, 30]
print([n for n in range(1,31) if n%2==0 and n%3==0]) # [6, 12, 18, 24, 30]

cubic = [x**3 for x in range(1,11) if x**3 <= 500]
print(cubic) # [1, 8, 27, 64, 125, 216, 343]

'''
isdigit() 함수 : 문자열이 숫자로만 이루어져 있는지를 검사하여 True/False 반환

문자열.isdigit()
: 숫자외에 공백이나 다른 문자가 포함 되어 있으면 False 반환
'''

st = 'Hello 1234 Python'
print([x for x in st if x.isdigit()]) # ['1', '2', '3', '4']

'''
iterator(반복자)란?
: 값을 차례대로 꺼낼 수 있는 객체
  __iter__()와 __next__() 메서드 가지고 있음
  
iter() 함수  -> 여기선 굳이 사용 X 나중에 클래스에서 사용함
: iter(iterable, [sentinel])
- iterable : 반복 가능한 객체(리스트, 튜플, 문자열 등)
- sentinel(옵션) : 반복자에 의해 반환되는 값 중에서 반복을 종료할 값 
  
next() 함수 
: 반복자의 메서드를 호출할 때마다 다음 값 반환
  더 이상 반환할 값이 없으면 예외 발생 -> StopIteration
  
** iter()함수는 반복 가능한 객체를 반복자로 변환,
   next()함수는 그 반복자에서 값을 하나씩 꺼내는 역할 **
'''
str = iter('1234') # 리스ㅌ 형 객체를 반복자로 만듦
print(next(str)) # 1 # next() 내장 함수를 사용하여 순회 함
print(next(str)) # 2
print(next(str)) # 3
print(next(str)) # 4
# print(next(str)) # 마지막 원소 반환 후에는 StopIteration을 반환함

l = [10,20,30]
l_iter = iter(l)
print(l_iter) # <list_iterator object at 0x000001A5EAEDC7F0>

# n = 100
# n_iter = iter(n)
# print(n_iter) # 반복불가능 자료형인 int -> 오류

l = [10,20,30]
l_iter = iter(l)
sentinel = object()
while True:
    elem = next(l_iter, sentinel)
    if elem is sentinel:
        break
    print(elem)
    
class OddCounter:
    ''' 1부터 증가하는 홀수를 반환하는 클래스 '''
    def __init__(self, n=1): # 초기화 메소드, n을 1로 둔다      # 생성자
        self.n = n
        # self : 클래스의 인스턴스(객체)자신을 가리키는 참조변수
        # self.n : 인스턴스 변수생성
        # 인스턴스 변수 : 객체 자식이 가지는 고유한 데이터를 저장하는 곳
    def __iter__(self): # 이 메서드가 정의되어 있으면, 해당 객체는 반복자(iterator) 됨
        return self 
    def __next__(self): # 반복자는 __next__() 함수를 가져야 함
        t = self.n # self.n을 임시 변수 t에 저장해 두고
        self.n += 2 # self.n을 2증가시킨다
        return t

# my_counter = OddCounter()
# print(next(my_counter)) # 1
# print(my_counter.__next__()) # 3
# print(next(my_counter)) # 5
# print(next(my_counter)) # 7

my_counter = OddCounter() # 객체가 생성될 때 자동으로 생성자 호출됨
for x in my_counter:
    if x>20: # 반복을 종료하는 조건 : x>20
        break
    print(x, end=' ') # 1 3 5 7 9 11 13 15 17 19

print()

# 짝수를 순차적으로 반환하는 __next__() 메소드를 가진 EvenCounter라는 클래스를 정의하고
# my_even 객체를 생성하여라
class EvenCounter:
    def __init__(self, n=0):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        t=self.n
        self.n=self.n+2
        return t
my_even = EvenCounter()
print(my_even.__next__(),end=' ') # 0
print(my_even.__next__(),end=' ') # 2
print(my_even.__next__(),end=' ') # 4
print(my_even.__next__(),end=' ') # 6
print(my_even.__next__(),end=' ') # 8

# 위 문제를 통해 생성한 my_even 객체를 이용하여 for 문에서 다음과 같이 20 이하의 짝수를 출력하여라
# 0 2 4 6 8 10 12 14 16 18 20
for x in my_even:
    if x>20:
        break
    print(x, end=' ') 
    
print()
    
# all() : iterator 항목들이 모두 참 -> True
l1=[1,2,3,4]
print(all(l1)) # 모든 요소가 0이 아니 -> True

l2 = [0,2,4,8]
print(all(l2)) # 한 요소만 0임 -> False

l3 = [0,0,0,0]
print(all(l3)) # 모든 요소가 0임 -> False

# split() 메소드
words='Python은 아름다운 언어입니다.'
words_list = words.split()
print(words_list) # ['Python은', '아름다운', '언어입니다.']

# join()으로 합치기 
# 사이에_넣을_문자.join(리스트)
time_str = '2019.02.20'
time_str_list = time_str.split('.')
print(time_str_list) # ['2019', '02', '20']
print('-'.join(time_str_list)) # 2019-02-20

txt = 'Welcome to Busan Metropolitan City'
print(txt.split()) # ['Welcome', 'to', 'Busan', 'Metropolitan', 'City']

greet = 'Hello,My name is DongMin,Good to see you again'
print(greet.split(',')) # ['Hello', 'My name is DongMin', 'Good to see you again']

fruits = 'Apple:Banana:Melon:Orange'
print(fruits.split(':')) # ['Apple', 'Banana', 'Melon', 'Orange']

import random
print(random.random())
print(random.uniform(3.5, 3.6)) # 3.5 와 3.6 사이의 랜덤 수
# randrange(a) : 0 <= x < a (정수형)
print(random.randrange(7))
# randint(a, b) : a <= x <= b (정수형)
print(random.randint(5,9))

L = [1,10, 100, 1000]
print(random.choice(L)) # 임의의 원소값 하나 반환
print(random.sample(L,2)) # 임의의 원소값 n개를 반환
random.shuffle(L)  # 목록 무작위 재배열 (반환 X)
print(L)

random.seed(0)
state = random.getstate()

print(random.sample(range(10), 5))




