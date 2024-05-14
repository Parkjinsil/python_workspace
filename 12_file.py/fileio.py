# file mode W r a
# write  : 쓰기모드 (w)
# read   : 읽기모드 (r)
# append : 추가모드 (a)

# 파일 객체 = open(파일 이름, 파일 열기 모드)
# f = open('새파일.txt','a') # 파일을 생성하기 위해 open함수 사용
# 'w'모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라짐

# f = open('C:/doit/새파일.txt','w') # 경로 안에 파일 생성
# f.write('I love python.')

# 열려 있는 파일 객체 닫아 주는 역할 (생략 가능)
# 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류 발생하기 때문에 써주는게 좋음
# f.close() 

# f = open('C:/doit/새파일.txt','w') # write시 data는 str type이어야 함
# for i in range(1,11):
#     data = '%d번째 줄입니다.\n' %i
#     f.write(data)
# f.close()

# readline() - 파일의 한 줄을 가져와 문자열로 반환
# readlines() - 파일 내용 전체를 가져와 리스트로 반환
#               각 줄은 문자열 형태로 리스트의 요소로 저장됨
# read() - 파일 내용 전체를 가져와 문자열로 반환

# readline()
f = open('C:/doit/새파일.txt','r')
while True:
    # \n
    line = f.readline()
    if not line: break
    print(line, end="")
f.close()

# readlines()
f = open('C:/doit/새파일.txt','r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()

# read()
f = open('C:/doit/새파일.txt','r')
data = f.read()
print(data)
f.close()

# with문 쓰면 close() 안 해줘도 됨
with open('c:/doit/새파일.txt','r') as file:
    content = list()
    
    # while True:
    #     sentence = file.readline()
        
    #     if sentence:
    #         content.append(sentence)
    #     else:
    #         break
    for f in file:
        content.append(f)
    
    for line in content:
        print(line, end='')
    
with open('c:/doit/새파일.txt','r') as file:
    # lines = file.readlines()
    # print(lines)
    lines = file.read()
    print(lines)
    
f = open('C:/doit/새파일.txt','a')
for i in range(11,20):
    data = '%d번째 줄입니다.\n' %i
    f.write(data)
f.close()    

with open('c:/doit/textfile.txt', 'w') as file:
    words = ['Python\n','YUNDAEHEE\n','076923\n']
    
    file.write('START\n') # 단일 문자열 작성
    file.writelines(words) # iterator을 문자열 목록으로 순차적으로 작성 가능
    file.write("END")
    
f = open('C:/doit/myfile.txt','r', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    raw = line.split()
    print(raw)
f.close()

with open('C:/doit/mytab.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        raw = line.strip().split('\t') # strip() 양쪽 빈칸 날림
        print(raw)