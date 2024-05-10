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
    
print(list(filter(func,range(-5,5))))

'''
filter에선 음수 -> False
bool에선 음수 -> True
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

