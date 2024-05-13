# print('Enter your name: ')
# name = input()
# print('Hello', name)

# number = input('숫자를 입력하세요 :')
# print(number)

# 한꺼번에 여러 개의 입력 값 받기 -> split()메소드 사용
# s1, s2 = input('문자열 2개를 입력하세요 :').split()
# print(s1)
# print(s2)

# num1, num2, num3 = input('세 정수를 입력하세요: ').split()
# # int() 함수를 이용해서 정수형으로 형 변환을 해야 함
# num1, num2, num3 = int(num1), int(num2), int(num3)
# print(num1, num2, num3, '세 정수의 합은 :',num1+num2+num3)

# 다중 데이터 입출력
# num1, num2, num3 = input('세 정수를 ,로 구분하여 입력하세요 : ').split(',')
# num1, num2, num3 = int(num1), int(num2), int(num3)
# print(num1, num2, num3,'세 정수의 합 :',num1+num2+num3)

print('hello'.upper())
print('HELLO'.lower())
print('Guido van Rossum'.split())
print('Apple,Banana,Orange'.split(','))
print('Apple|Banana|Orange|Kiwi'.split('|'))

# eval() 함수 : 스크립트 자체를 수행하는 등 기능이 매우 강력!
#               str형 데이터, 즉 텍스트를 바로 파이썬 코드로 변환함
#               사용 자제 권고!
print(eval('10+20')) # 30
print(chr(65)) # A
print(ord('A')) # 유니코드 값 반환 # 65

# su1 = eval(input('su1 :')) # 100 입력
# su2 = eval(input('su2 :')) # 200 입력
# print(su1+su2) # 300

print(eval('5**2*3-25')) # 50

def fun():
    print('나는 fun() 함수의 실행 결과입니다.')

# re = eval(input('아무거나 입력해보아요 :')) 
# 여기에 fun() 입력하면 '나는 fun() 함수의 실행 결과입니다.' 출력됨

# cr = input('3명의 국어점수(예 51,67,98)입력 :')
# k1,k2,k3 = eval(cr)
# print(k1,k2,k3,'합계 :',k1+k2+k3) # 90 87 81 합계 : 25

# 3개의 콤마로 구분된 정수를 입력 받아 평균을 출력해줍니다.
# num1, num2, num3 = input('콤바로 구분된 정수 3개를 입력하세요 :').split(',')
# num1, num2, num3 = int(num1), int(num2), int(num3)
# print('평균 :',(num1+num2+num3)/3)

# lst = input('콤바로 구분된 정수 3개를 입력하세요 :').split(',')
# int_list = [int(x) for x in lst]
# print(sum(int_list)/len(int_list))
    
# 곱할 숫자 1과 곱할 숫자2를 입력받아 곱을 구하시오
# a = float(input('곱할 숫자 1 :'))
# b = float(input('곱할 숫자 2 :'))
# result = a*b
# print('{0} x {1} = {2}'.format(a,b,a*b))

# 문자열 띄어쓰기
print('life', 'is', 'too short')
# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')
print()

# 포맷팅
greet = 'Hello'
print('{} World!'.format(greet))

# format() 메소드를 사용하지 않는다면 출력문은 복잡한 형태로 나타남.
# 이 경우 쉼표가 너무 많고 따옴표도 많아서 코드를 읽기도 힘들고 오류가 날 가능성도 매우 높음
# name = input('당신의 이름을 입력해주세요 :')
# age = input('당신의 나이를 입력해주세요 :')
# job = input('직업을 입력해주세요 :')
# print('당신의 이름은 {}, 나이는 {}살, 직업은 {}입니다.'.format(name,age,job))

# name = input('당신의 이름을 입력해주세요 :')
# age = input('당신의 나이를 입력해주세요 :')
# job = input('직업을 입력해주세요 :')
# address = input('사는 곳을 입력해 주세요 :')
# print('당신의 이름은 {}, 나이는 {}살, 직업은 {}, 사는 곳은 {}입니다.'.format(name,age,job,address))
# print('당신의 이름은',name,'나이는',age,'직업은',job,'사는 곳은',address,'시입니다.')

# 고급 format() : 자릿수 맞추고 싶을 때
for i in range(2,15,2):
    print('{0} {1} {2}'.format(i,i*i,i*i*i)) # 이렇게 하면 보기 불편함

for i in range(2,15,2):
    #         출력 칸 수 지정
    print('{0:3d} {1:4d} {2:5d}'.format(i,i*i,i*i*i)) # 이렇게 하면 오른쪽 정렬된 보기 좋은 출력

# {0:5.2f} -> 전체 5자리중에 소수점 아래 2만 출력
print('소수점 두 자리로 표현한 원주율 = {0:5.2f}'.format(3.1415926)) # (  3.14)
print('{:,}'.format(1234567890)) # 1,234,567,890   # 1000 단위 쉼표 출력

# 위도 : 35.17N, 경도 : 129.07E
print('위도 : {lat}, 경도 : {long}'.format(lat='35.17N',long='129.07E'))
# 경도 : 129.07E, 위도 : 35.17N
print('경도 : {long}, 위도 : {lat}'.format(lat='35.17N',long='129.07E'))

# input1 = int(input('첫번째 숫자를 입력하세요 :'))
# input2 = int(input('두번째 숫자를 입력하세요 :'))
# total = input1+input2
# print('두 수의 합은 %d 입니다.'% total)

# 65, 45, 2, 3, 45, 8
lst = input('정수 6개를 ,로 구분하여 입력하시오 :').split(',')
int_lst = [int(x) for x in lst]
print('총합 :',sum(int_lst))

