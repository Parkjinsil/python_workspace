import numpy as np
'''
반복문
for : 반복 "횟수"가 명확한 경우
while : 반복 횟수는 알지 못하지만 반복하는 "조건"이 명확한 경우에 사용

형식
초기값 지정
while 조건식:
    실행할 코드 블록
    
break : 반복문 즉시 종료
'''

i=1
sum=0
while i<=10:
    sum+=i
    i+=1
    
print('1부터 10까지의 합은',sum)

st = 'Programming'
for ch in st:
    if ch in ['a','e','i','o','u']:
        break # 모음일 경우 반복문 종료
    print(ch)
print('The end')

# continue : 아래에 있는 나머지 부분을 실행X 반복문의 처음으로 돌아감
st = 'Programming'
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
print('The end')

# prompt = """
#     1. Add
#     2. Del
#     3. List
#     4. Quit

#     Enter number: """
# number = 0
# while number!=4:
#         print(prompt)
#         number = int(input())
        
# coffee = 3
# while True:
#     money = int(input('돈을 넣어주세요 : '))
#     if money==300:
#         print('커피를 줍니다')
#         coffee = coffee-1
#     elif money>300:
#         print('거스름돈 %d를 주고 커피를 줍니다'%(money-300))
#         coffee = coffee-1
#     else:
#         print('돈을 다시 돌려주고 커피를 주지 않습니다')
#         print('남은 커피의 양은 %d개 입니다'%coffee)
#     if coffee==0:
#         print('커피가 다 떨어졌습니다. 판매를 중지 합니다')
#         break
    
sum = 0
for x in range(1,101):
    sum+=x
print('1부터 100까지의 합 :',sum)

i = 0
sum = 0
while i<100:
    i=i+1
    sum +=i
print('1부터 100까지의 합 :',sum)

i = 1
sum = 0
while i<1001:
    if i%3==0:
        sum+=i
    i=i+1
print('1부터 1000까지의 자연수 중 3의 배수의 합 :',sum)

for x in range(2, 10):
    for y in range(1, 10):
        print('%d * %d = %d'% (x,y,x*y))
        

# range 함수 : 숫자 리스트를 자동으로 만들어 주는 함수
#              int만 가능. float를 위해서는 NumPy의 arage() 사용
# range(start, end, step) : start 이상 end 미만 step 간격으로

 
# range() 함수와 list() 함수를 사용하여 1 이상 100 이하의 자연수 리스트를 만드시오.
print(list(range(1,101)))

# 1 이상 100 이하의 짝수 리스트
print(list(range(2,101,2)))

# 1 이상 100 이하의 홀수 리스트
print(list(range(1,101,2)))

# -100보다 크고 0보다 작은 음수 리스트
print(list(range(-99,0)))

'''
arange() 함수 : range() 함수와 유사하지만 NumPy 배열을 생성하는 데 사용됨
                터미널에 pip install numpy 로 설치
                import numpy as np(별칭)
                작업할 데이터가 순차적으로 배열 형태로 필요한 경우 유용
                ex) 선형공간에서 데이터를 생성 / 반복 작업 수행할 때
                
numpy.arange(start, end, step, dtype=None)
    start(선택) : 시작 값(기본값:0)
    end(필수)  : 포함X
    step(선택) : 간격(기본값:1)
    dtype(선택) : 반환된 배열의 데이터 유형

NumPy 배열 : NumPy 라이브러리에서 제공하는 고성능 다차원 배열 객체
            list랑 비교했을 때 메모리 효율성과 속도 면에서 크게 우위를 가지고 있음
            특히 대용량 데이터 처리나 과학/공학 분야 계산에 많이 사용됨
특징
- 동종 데이터 타입으로 구성
- 규칙적인 메모리 레이아웃을 가지고 있어 효율적인 계산 가능
- 벡터 및 행렬 연산을 위한 다양한 함수와 메서드를 제공
- 반복문 없이 데이터 배열 전체에 대한 작업을 수행할 수 있어 속도가 매우 빠름(벡터화 연산)
- 다양하나 차원의 배열을 표현할 수 있음(1차원, 2차원, 3차원, ...)
'''
print(list(np.arange(0,10,0.5)))

# [-2, -4, -6, -8]
print(list(range(-2, -10, -2)))

# print() 함수의 end 키워드 인자 
# end 는 출력될 값들 이후에 어떤 문자열을 추가할지를 지정하는 매개변수 / 기본값: \n(줄바꿈)
for i in range(5):
    print(i,end =' ') # 0 1 2 3 4
print()
    
a = [(1,2),(3,4),(5,6)] # 튜플
for (a, b) in a:
    print(a+b)

marks = [90, 25, 67, 45, 80]
number = 0
for number in range(len(marks)): # range(5) 0...4   
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))
    
# for else문 : for문이 끝까지 실행되어 종료됐을 때, else구문으로 넘어감
#              중간에 중단(break)되면 else구문 실행 X
for i in range(3): # 0.1.2
    print('i =',i)
else:
    print("END")
    
for j in range(3):
    if j==2:
        break
    print('j =',j)
else:
    print("END") # 출력 안 됨
    
# while문에서 continue 구문 잘 못 사용할 경우 '무한 루프'에 빠질 수 있음

for i in range(5):
    print("Hello, Python!")
    
for i in range(5):
    print(i)
    
'''
enumerate : 순서를 같이 출력하고자 할 때
            열거형(enumerate)은 반복자(ieterator)를 지원하는 객체를 index 값과 요소 값을 동시에 반환하는 객체
'''

# 0 A
# 1 B
# 2 C
names = ["A", "B", "C"]
for x, name in enumerate(names):
    print(x, name)
    
'''
zip : 길이가 같은 두 개의 리스트를 for문에서 같이 돌릴 때
'''

names = ["A", "B", "C"]
scores = [70, 80, 90]

# 0 A 70
# 1 B 80
# 2 C 90
for i, (name, score) in enumerate(zip(names, scores)):
    print(i, name, score)
    
# 루프 제어변수의 익명화
# : 반복문에서 새롭게 할당되는 변수 i는 실행문에서 사용되지 않는 루프변수이므로 다음과 같이 언더스코어(_)를 대신 넣어서 익명화 시킬 수 있음

for _ in range(10):
    print("Welcome to everyone!")
    
'''
리스트 내포(List comprehension) 
: [표현식 for 항목 in 반복가능객체 (if 조건)]
'''
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

result = [num*3 for num in a if num%2==0]
print(result)

# 구구단을 매우 쉽게 만들 수 있음.
# 리스트에 따로 담을 필요도 없음.
result = ['%d x %d = %d'%(x,y,x*y) for x in range(2,10) if x in (3,5)
                                   for y in range(1,10) if y in (4,8)]
print(result)

# 1부터 100까지 출력
result = [i for i in range(1,101)]
print(result)

# 5의 배수의 총합
sum = 0
for num in range(1, 1001):
    if num%5==0:
        sum += num
print(sum)

# 학급의 평균 점수
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for a in A:
    sum +=a 
print(sum/len(A))

# 각 혈액형 별 학생수의 합계
blood_type = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
print('A형 학생수 :',blood_type.count('A'))

numbers = [1,2,3,4,5]

result = []
for n in numbers:
    if n%2==1:
        result.append(n*2)
# 위 코드를 리스트 내포를 이용하여 표현해라
result = [n*2 for n in numbers if n%2==1]
print(result)