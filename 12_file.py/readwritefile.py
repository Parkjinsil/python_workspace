# f1 = open('test.txt','w')
# f1.write('Life is too short')

# f2 = open('test.txt','r')
# print(f2.read())

# file = open('test.txt','a')
# line = input('저장할 내용을 입력하세요:')
# file.write(line+'\n')
# file.close()

# replace 함수
# rfile = open('test.txt','r')
# data = rfile.read()
# rfile.close()

# data = data.replace('java','python')

# wfile = open('test.txt','w')
# wfile.write(data)
# wfile.close()

with open('sample.txt','r') as file:
    # line string
    total = 0
    count = 0
    for line in file:
        num = int(line)
        total += num
        count +=1
    average = total/count
    print('total :',total, 'average :',average)   
       
with open('result.txt','w') as wfile:
    wfile.write('total : %d, average : %d'%(total,average))