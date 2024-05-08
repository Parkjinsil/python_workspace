'''
lamda 함수 : 익명 함수(anonymous funcion)를 만들 때 사용하는 방법
             일회용 간단한 함수를 작성할 때 유용
             복잡한 로직은 일반 함수로 작성하는 것이 가독성이 좋음
             lambda는 한 줄로 표현되어야 하므로 여러 줄의 코드가 필요한 경우에는 일반 함수 사용해야 함

기본 구문
-> lambda 인자들: 표현식
   인자들 : 매개변수 (여러 개 가능)
   표현식 : lambda 함수가 계산하고 반환할 값
'''

'''
sorted() 함수
매개변수
1) iterable(필수) : 정렬할 iterable 객체(리스트, 튜플, 문자열 등)
2) key(선택) : 각 요소를 어떤 기준으로 정렬할지 결정하는 함수를 지정
3) reverse(선택) : True이면 내림차순, False(기본값)이면 오름차순

sorted() vs sort()
sorted() 함수는 원본 iterable은 변경하지 않고, 정렬된 새로운 리스트 반환함
sort()는 원본을 정렬
'''

# Value를 기준으로 오름차순 정렬
a = { 5 : '서울', 3 : '부산', 2 : '광주', 10 : '경남'}
sorted_a = sorted(a.items(), key=lambda x:x[1])
# -> lamda식에 x인자에 a.items()를 넣어주는건 
#    sorted()에서 key가 sorted 각 항목을 어떤 값을 기준으로 정렬할지 결정하는 함수를 받는 거라서
#    sorted()내부적으로 대입해주는거임
# [(10, '경남'), (2, '광주'), (3, '부산'), (5, '서울')]
print('value로 정렬 : ',sorted_a) 

n_list = list(range(15))
s_listx = n_list[6:11]
s_list5 = s_listx[::-1]
# 위 두 문장을 한 문장으로
s_list5 = n_list[10:5:-1]  # -> 10은 시작 인덱스 , 5는 종료 인덱스(포함X), -1은 step값으로, 뒤에서부터 요소를 선택
print(s_list5) # [10, 9, 8, 7, 6]

a =list(range(10))[-3::-1] 
# 1) [-3::-1]  -> 정답 : 뒤에서 세 번째 인덱스부터 시작인덱스까지(종료인덱스 없으므로) 뒤에서부터 선택해라
# 2) [3::2]    -> [3, 5, 7, 9]
# 3) [7:0]     -> []
# 4) [-2::-1]  -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a) # [7, 6, 5, 4, 3, 2, 1, 0]