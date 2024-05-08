import copy
# Dictionary : 대응 관계를 나타내는 자료형
#              Key, Value 한 쌍으로 가짐
#              Key는 고유한 값(unique), 변하지 않는 값 사용
#              순차적으로 해당 요소값 구하지 않음 -> index X
#              {}으로 표시

a = {
    "name" : "pey",
    "phone" : "01199993323",
    "birth" : "1118"
}
print(a)
print(a["name"]) # pey
print(a.get('name')) # pay

# 새로운 키:값의 항목 삽입
person = {'이름':'홍길동', '나이':26, '몸무게':82}
# person['직업'] = '율도국의 왕' # {'이름': '홍길동', '나이': 26, '몸무게': 82, '직업': '율도국의 왕'}
print(person)
# 여러 값의 항목 삽입 : update
person.update({'주소': '문정동', '강아지':'소망이'})


# 삭제
# del person['나이'] # {'이름': '홍길동', '몸무게': 82}
print(person)

# 주의할 사항
# 중복되는 Key 사용 X
# Key에 리스트는 쓸 수 X but 튜플은 Key로 쓸 수 O

# a.keys() : 딕셔너리 a의 key만 모아서 dict_keys라는 객체 리턴함
# a.values() : value만 모아서 dict_keys 객체 리턴
# a.items() : 쌍으로 얻음 (tuple)
# a.clear() : 모두 삭제

# 정렬 : Key를 기준으로 오름차순 정렬
a = { 5 : '서울', 3 : '부산', 2 : '광주', 10 : '경남'}
sorted_a = sorted(a) # [2, 3, 5, 10]
sorted_a = sorted(a.items()) 
# [(2, '광주'), (3, '부산'), (5, '서울'), (10, '경남')]
print('key로 정렬 : ',sorted_a)

# Value를 기준으로 오름차순 정렬
sorted_a = sorted(a.items(), key=lambda item:item[1])
# [(10, '경남'), (2, '광주'), (3, '부산'), (5, '서울')]
print('value로 정렬 : ',sorted_a) 

# 수정
# 사전[key] = value
# 사전.update(key=value)

# 삭제
# del 사전['key]
# 사전.pop['key']
# 사전.popitem() -> 마지막 요소 삭제

# 'C'에 해당되는 키값이 없을 경우 오류 대신 70을 얻을 수 있도록 수정해 보자
a = {'A':90, 'B':80}
print(a.get('C', 70))

a = {'A':90, 'B':80, 'C':70}
print('최소값 : ',min(a.values()))
print('최대값 : ',max(a.values()))

fruits_dic = {
    'apple':6000,
    'melon':3000,
    'banana':5000,
    'orange':7000
}

print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))

print('항목의 개수 :',len(fruits_dic))

if 'apple' in fruits_dic:
    print('apple is in fruits_dic')

if 'mango' not in fruits_dic:
    print('mango is not in fruits_dic')
    
# Set(집합형) : Key가 없는 Dictionary , 중복 X
test_set = set()
print(test_set)

set1 = {1,2,3,4} # 집합
set2 = set({1,2,3,4}) # 튜플 -> 집합
set3 = set([1,2,3,4]) # 리스트 -> 집합

print(set1)
print(set2)
print(set3)

s1 = set([1,2,3,4,5,6])
s2 = {4,5,6,7,8,9}

# 교집합
print('s1 & s2 : ', s1 & s2)
print(s1.intersection(s2))

# 합집합
print('s1 | s2 : ', s1 | s2)
print(s1.union(s2))

s1 = set([1,2,3])
s1.add(4) # {1, 2, 3, 4}
print(s1)
s1.remove(2)
print(s1) # {1, 3, 4}

s = {100, 100, 200, 200, 300, 300, 400}
print(s) # {200, 100, 400, 300}

s.add(500)
print(s) # {100, 200, 300, 400, 500}

list1 = ['a', 'b', 'c']
s1 = set(list1)
print(s1) # {'b', 'c', 'a'} -> 집합 자료형

list2 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s2 = set(list2)
print(s2) # {1, 2, 3, 4, 5}

s1 = set(['a', 'b', 'c', 'd', 'e'])
s2 = set(['c', 'd', 'e', 'f', 'g'])
print(s1-s2) # {'a', 'b'}

s3 = {}
print(type(s3)) # 'dict'
s4 = set()
print(type(s4)) # 'set'

a = {'a', 'b', 'c'}
a.update('d', 'e', 'f')
print(a)

# 변수 : 변수는 메모리 주소를 가리키는 포인터
a = 3
print(id(a)) # 140722743941624

b = a        # 주소 복사
print(id(b)) # 140722743941624(a와 동일)

print(a is b) # True

a = 4
print(id(a)) # 140722743941656 (바뀜)
print(id(b)) # 140722743941624 (원래와 동일)

print(a) # 4 (a 값만 바뀜)
print(b) # 3 

# List
a = [1,2,3]
print('id(a)= ',id(a)) # 1946185381632

b = a # 리스트에서 =는 값을 넣는 게 아니고 주소를 공유함
print('id(b)= ',id(b)) # 1946185381632(a와 동일)

print(a is b)
a[0] = 4
print('id(a)= ',id(a)) # 1946185381632(동일)
print('id(b)= ',id(b))  # 1946185381632(동일)

print(a)
print(b) # b도 [4,2,3]으로 바뀌어버림

'''
List 복사
그냥 복사하면 같은 주소값을 가리키므로 
원래 list를 바꿔버리면 복사list도 따라서 바뀜
그럴 땐 b = a.deepcopy() 사용해라!
'''

a = [1,2,3]
print('id(a) = ',id(a)) # 2152507851968
b = a[:] # slice 리스트 복사의 경우 주소 복사가 아닌 값 복사!!
print('id(b) = ',id(b)) # 2152507851648 (달라짐)
print(a)
print(b)

print('-----------------------------')

a[0]=4
print('id(a) = ',id(a))
print('id(b) = ',id(b))
print('a : ',a) # [4, 2, 3] (a만 바뀜)
print('b : ',b) # [1, 2, 3]

# copy도 리스트 값 복사

s = [1, 2, 3, [4, 5, 6]]
c = s[:]
c[3][0] = 'c'
c[0] = 'x'
print(s) # [1, 2, 3, ['c', 5, 6]]
print(c) # ['x', 2, 3, ['c', 5, 6]]
# list 안에있는 list는 복사하면 주소값이 복사돼버려서 오류가 생김
# -> 이럴 때는 deepcopy 쓰면 됨

s1 = [1,2,3,[4,5,6,[7,8,9]]]
c1 = copy.deepcopy(s1)
c1[3][0] = 'c'
c1[3][3][0] = 'z'
c1[0] = 'x'
print('c =',c1) # ['x', 2, 3, ['c', 5, 6, ['z', 8, 9]]]
print('s =', s1) # [1, 2, 3, [4, 5, 6, [7, 8, 9]]]

[a, b] = ['python', 'life']
print('a =',a)
print('b =',b)

a = [1,2,3]
b = [1,2,3]
print(a is b) # False -> 주소값 비교
print(a == b) # True -> 값 비교

a = [1,2,3]
b = a
print(a is b) # True

a = [1,2,3]
b = a[:]
print(a is b) # False

