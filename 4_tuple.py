# Tuple : immutable(변경 불가능)                /  List : mutable(변경 가능)
#   ()    문자열도 immutable                        []
#         그래서 sort(), append() 등의 메서드 사용 불가

tup = (100,) # 반드시 ',' 써줘야 함, 하나만 쓰면 그냥 int 타입 돼버림
print(type(tup))
print(tup)

# 패킹packing 언패킹unpacking
a = (1, 2) # 패킹
b, c = a  # 언패킹 
print(b) # 1
print(c) # 2

def multif(a, b):
    return (a+b, a*b)

(sum, mul) = multif(10, 20) # 언패킹
print(sum)
print(mul)

# 스왑(swap) 
a = 100
b = 200
a, b = b, a
print('a = ',a, 'b = ',b)

# 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0]) # 1
print(t1[3]) # b

# 슬라이싱
print(t1[1:]) # (2, 'a', 'b')

# 튜플과 정수는 덧셈 연산 X

# 튜플과 하나의 요소를 가진 튜플의 덧셈 연산
t0 = (10, 20, 30)
t1 = t0 + (40,)
print(t1) # (10, 20, 30, 40)

# 튜플 변환
a = tuple("abcde")
print(a) # ('a', 'b', 'c', 'd', 'e')

# 리스트 변환
b = list("abcde")
print(b) # ['a', 'b', 'c', 'd', 'e']

# in : 리스트 튜플, 집합, 딕셔너리 광범위 하게 사용
tup = ('1', 'b', 'c')
if 'b' in tup:
    print('b는 튜플 안에 있습니다.')
else:
    print('b는 튜플 안에 없습니다.')
    
for x in range(1, 11):
    print(x) # 1~10까지 출력됨
    
# 구구단 출력
for x in range(2, 10):
    for y in range(1, 10):
        print('%d x %d = %d'%(x, y, x*y))
        
t_fruits = ('apple', 'orange', 'water melon')
print('t_fruits :', t_fruits)

f_list = list(t_fruits) # 튜플을 리스트로 전환
f_list[1] = 'kiwi' # 리스트의 두 번째 항목 값을 'kiwi'로 변경
tt_fruits = tuple(f_list) # 리스트를 튜플로 다시 반환
print('tt_fruits : ',tt_fruits)

# 숫자 3만을 요소값으로 가지는 튜플을 작성해라
t = (3,) # ',' 반드시 써줘야 함

# (1, 2, 3)이라는 튜플에 4라는 값을 추가하여 (1, 2, 3, 4)처럼 만들어 출력해 보자
# append 대신에 튜플 더하기 사용
t = (1, 2, 3)
t1 = t+(4, )
print(t1)

