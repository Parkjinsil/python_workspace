arr = [4,4,4,3,3]
answer = []
answer_list = []
for a in range(1,len(arr)):
    if arr[a]==arr[a+1]:
        answer.append(a)
        print('a',a)
        print(arr)
    if len(arr)-1<a:
        break
print(answer)

for a in answer:
    answer_list.append(arr[a])
print(arr)



