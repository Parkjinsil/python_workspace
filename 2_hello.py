print("Hello World")
# 여기는 주석이예요.
a = 10
if a == 10: # 이 경우는 a가 10일 경우 임
    print("어쩌고저쩌고")
elif a == 20:
    print("어째저째")
    
# Ctrl + /
# 나는 한국 사람 입니다.
# 너는 미국 사람 입니까?

'''
이 함수는 두 값의 평균을 구하는 함수 입니다.
이름은 average입니다.
파라미터는 a, b 입니다.
리턴 값은 두 값의 산술평균입니다.
'''
def average(a, b):
    return (a+b)/2

print('나의 이름은 : ', '홍길동')
print('나의 이름은 : ', 27)
print('나의 키는', 179, 'cm입니다.')
print('10 + 20 =', 10+20)
print('10 * 20 =', 10*20)
print('10과 20의 평균값은', average(10, 20))

radius = 4.0
print('원의 반지름', radius)
print('원의 면적', 3.14 * radius * radius)
print(id(radius)) # 주소값
white = 0xFFFFFF
print(white)

# ** : 제곱

print('123 + 456 = ', 123+456)
print('1357 + 2468 = ', 1357+2468)
print('5**4', 5**4)
print('10 / 4 = ', 10/4) # 나누기
print('10 // 5= ', 10//5) # 몫
print('10 % 5 = ', 10%5) # 나머지

print('5를 2로 나눈 나머지 : ', 5%2)
print('2의 제곱근 루트2 : ', 2**0.5, '3의 제곱근 루트3 : ', 3**0.5)


korean = 80
english = 75
math = 55

average = (korean + english + math)/3
print('홍길동 씨의 평균 점수 : ', average, '입니다.')

def answer(n):
    if n%2==0:
        return '짝수입니다.'
    else :
        return '홀수입니다.'

print(answer(13))
        