# 큰 따옴표, 작은 따옴표 상관 X
txt1 = '강아지 이름은 "소망"이야'
print(txt1)

txt2 = "강아지 이름은 '소망'이야"
print(txt2)

# 큰(작은) 따옴표 안에 큰(작은)따옴표를 넣으려면 백슬래쉬를 앞에 써줌
txt3 = "친구가 \"소망이가 좋아\"라고 말했다"
print(txt3)

# 개행(줄바꿈) : \n
# 윈도우 \n
# 유닉스 \n\r
txt5 = 'banana\napple\norange'
print(txt5)

# 문자"\" : \\
    
a1 = r'\n'
print(a1) # \n 출력됨
# Raw 날것 원형 그대로 

head = "파이썬"
tail = "은 재밌다"
print(head+tail)
print(head*5)

# 평점 start
star = '*'
score = 4
print(star*score)

# 인덱싱 0부터 시작
a = 'Life is too short, You need Python'
print(a[0])
b = '인생은 짧다. 너는 파이썬이 필요하다'
print(b[13])

print(a[-1])
print(b[-1])

social_no = '971017-2080018'
sex_type = social_no[7]
if sex_type == '1' :
    print('남자입니다')
else :
    print('여자입니다')
    
date = '2024-05-07'
#       0123456789
year = date[0:4] # 0부터 3까지 (0부터 4까지 X)
month = date[5:7]
day = date[-2:] # date[8,] / date[8,10]
print('year:',year, 'month:', month, 'day:', day)

# sri = "서울특별시 서대문구 증산로"
sri = '경상남도 창원'
idx = sri.find(' ')
sido = sri[0:idx]
print('['+sido+']')

# String은 Mutable <-> Immutable

greeting = "나는 한국인 입니다"
# greeting[0] = "저" -> 이렇게 불가능
greeting2 = "저"+greeting[1:]
print(greeting2)

# 문자열 포맷팅 : 출력 시 변수를 포함하는 문자열의 형식을 지정
print("I eat %d apples" %3) # I eat 3 apples
print("나는 사과는 %d개 먹고 바나나는 %d개 먹었습니다." %(3, 2))

print("I eat {} apples {} bananas".format(2, 3)) # I eat 2 apples 3 bananas
print("I eat {1} apples {0} bananas".format(2, 3)) # I eat 3 apples 2 bananas -> 자리 표시해주면 순서 바꿀 수 있음

print("I eat {} apples".format("five"))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days".format(number, day))

print("I ate {number} apples. so I was sick for {day} days".format(number=11, day=12))

y = 3.42134234
print("{0:0.4f}".format(y)) # 3.4213 

# 길이
a = "나는 한국인 입니다."
print(len(a))

# 숫자 세기
b = "hobby"
print(b.count("b"))

# 위치 알려주기 1 : 문자열 중 문자 "b"가 처음으로 나온 위치를 반환 / 만약 없으면 -1 반환
a = "Python is the best choice."
c = a.find("b")
print(c)

# 문자열 삽입 - join
sri = "abcd"
sri2 = ",".join(sri)
print(sri2)

print(",".join("ABCD"))

# 공백 지우기 - strip
print(" hello ".rstrip())
print(" hello ".lstrip())

# 문자열 바꾸기 - replace (있는 거 모두 바꿔줌)
s1 = 'Long live the King King!'
s2 = s1.replace("King", "Queen")
print(s2)

# 문자열 나누기 - split
a = "Life is too short."
print(a.split())
b = "a:b:c:d"
print(b.split(':'))


no = "881120-1068234"
print(no.split("-"))

pin = "881120-1068234"
sex_type = pin[7]
print(sex_type)

sri = "a:b:c:d"
print(sri.replace(":", "#"))

url = "http://naver.com"
url1 = url.replace('http://','') # naver.com
url2 = url1[:url1.find('.')] # naver
url3 = url2[:3]+str(len(url2))+str(url2.count('e'))+"!"
print(url3) # nav51!

'''
int를 String으로 : str.()
ex) str.(url1) 
단, str을 변수명으로 사용했으면 오류가 날 수 있음
''' 

'''
list1 = list()
list2 = []
list3 = list((1,2,3))
list4 = [1,2,3]
list5 = list(range(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list5)
'''

list1 = [2, 4, 6, 8, 10]
list2 = []
list2.append(2)
list2.append(4)
list2.append(6)
list2.append(8)
list2.append(10)
print(list2)

# range(start : stop : step)   /  stop 값은 포함 X
rangelist = list(range(2, 11, 2)) # [2, 4, 6, 8, 10]
print(rangelist)

# Prime Number 소수
# 2, 3, 5, 7
prime_list = [2, 3, 5, 7]
print(prime_list[0])
print("prime_list의 마지막 원소 : ",prime_list[len(prime_list)-1])
print("prime_list의 마지막 원소 : ",prime_list[-1])

n_list = list(range(15)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(n_list)

s_list1 = n_list[:5] # [0, 1, 2, 3, 4]
print(s_list1)

s_list2 = n_list[5:11] # [5, 6, 7, 8, 9, 10]
print(s_list2)

s_list3 = n_list[11:] # [11, 12, 13, 14]
print(s_list3)

s_list4 = n_list[2:11:2] # [2, 4, 6, 8, 10]
print(s_list4)

s_listx = n_list[6:11]
s_list5 = s_listx[::-1] # [10, 9, 8, 7, 6]
print(s_list5)

n_list = [11, 22, 33, 44, 55, 66]
print(n_list)
del n_list[3] # [11, 22, 33, 55, 66]
print(n_list)

'''
pop()와 remove()함수의 차이
pop() : 디폴트로 리스트의 제일 마지막 항목을 삭제한 후 "이 항목"을 반환
remove() : 삭제만 하고 반환값 X -> NONE   
'''
# remove()
n_list.remove(11)
print('remove(11)한 후',n_list)
print('pop()한 후 ',n_list.pop())
print(n_list)
# pop

a = ["한국", "일본", "중국"]
print(a.index("일본")) # 1
a.append(["미국", "영국"]) # ['한국', '일본', '중국', ['미국', '영국']]
print(a) 
a.extend(["미국", "영국"]) # ['한국', '일본', '중국', '미국', '영국']
print(a)
a.pop()


n_list = list(range(1,11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n_list)
n_list.insert(0,0) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n_list)

a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(a[4], a[2]) # you too

b = ['Life', 'is', 'too', 'short']
print('['+b[0],b[1],b[2],b[3]+']') # Life is too short
print(' '.join(b))

a = [1, 2, 3]
print(len(a)) # 3


a = [1, 3, 5, 4, 2]
a.sort() # [1, 2, 3, 4, 5]
a.reverse() # [5, 4, 3, 2, 1]
print(a) 

a = [1, 2, 3, 4, 5]
print(a[0::2]) # [1, 3, 5]



