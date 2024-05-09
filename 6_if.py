'''
조건문
제어문 마지막은 콜론(:)으로 끝냄
실행 블록은 들여쓰기!!!
'''

# game_score = int(input('점수를 입력하세요 : '))
# if game_score >= 1000:
#     print('당신은 고수입니다')
    
num_a = 100
num_b = 200
if num_a==num_b:
    print('두 값이 일치합니다.')
else :
    print('두 값이 일치하지 않습니다.')
    

# n = int(input('정수를 입력하세요 : '))
# print('n =',n)
# if n%2==0:
#     print(n,'은 짝수입니다.')
# else :
#     print(n,'은 홀수입니다.')
    
# x = int(input('정수를 입력하세요 : '))
# print('x =',x)
# if x>0:
#     print(x,'는 자연수입니다.')
    
num = 100
if num<0:
    print('음수입니다.')
else :
    print('양수입니다.')
    if num%2==0:
        print('짝수입니다')
    else :
        print('홀수입니다.')
        
'''
블록(block)
: 어떤 조건을 만족하는 경우에 특정한 코드를 선택적으로 실행하는 구조
: 실행 코드
: 블록은 반드시 들여쓰기를 해야한다!!!
*** 파이썬은 들여쓰기가 매우 중요한 의미를 가지는 프로그래밍 ***
'''

a = 10
b = 14
if (a%2==0) and (b%2==0): # 첫번째 조건문
    print("두 수 모두 짝수 입니다.")
    
if (a%2==0) or (b%2==0) :
    print('두 수 중 하나 이상이 짝수입니다.')
    
num = 2
if (num>1) and (10>num):
    print('True')

age = 11
if (age>10) and (age<19):
    print('청소년입니다.')
    
# score = int(input('점수를 입력하세요 : '))
# if score>=90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else :
#     print('F')

# speed = int(input('자동차의 속도를 입력하세요(단위: km/h) : '))
# if speed>=100:
#     print('고속')
# elif speed>=60:
#     print('중속')
# else :
#     print('저속')
    
# 조건문에서 아무 일도 하지 않게 설정하고 싶다면 -> pass

# 조건부 표현식
# 조건문이_참인_경우 if 조건문 else 조건문이_거짓인_경우
# message = "success" if score >= 60 else "failure"
# 가독성에 유리하고 한 라인으로 작성할 수 있어 활용성이 좋다.

money = 3000
card = True
if (money>=4000) or (card):
    print('택시를 탈 수 있습니다.')
    
lucky_list = [1,9,23,46]
hong = 23
if hong in lucky_list:
    print('야호')    
    
age = 30
height = 180
if (age<30) and (height>=175):
    print('YES')
else :
    print('NO')


