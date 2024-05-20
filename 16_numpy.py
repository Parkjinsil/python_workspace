'''
Numpy
- 다량의 수치 데이터를 다루고, 일부를 추출하는 데에 효율적
- 강력한 배열 프로그래밍 기능
  -> 데이터에 연산을 실시할 때, 데이터를 구성하는 값 전체에 대해 한 번에 연산이 적용되도록 하는 방식
  -> 배열 프로그래밍은 데이터를 다루는 연산의 표현을 간결하게 만듦
- 다차원 데이터 저장에 강점

Array(배열)
: Numpy 배열은 "동일한" 자료형을 가지는 값들이 격자판 형태로 있는 것
: 각각의 값들은 양의 정수 튜플로 색인(indexing)
: List와 유사하나 List는 이종의 자료형이 가능하고, 수치연산의 형태가 상이함

'''
import numpy as np

# 넘파이 배열을 생성할 때 반드시 대괄호를 사용하여 리스트 형식의 데이터를 만들어서 인자로 넣어야함
a = np.array([1,2,3])
print(a.shape)          # (3,) shape은 생성된 배열객체의 형태를 튜플 타입으로 반환함
print(a.ndim)           # 1
print(a.dtype)          # int32
print(a.size)           # 3
print(a.itemsize)       # dtype byte size
# int 32 32/8 = 4 4byte integer 4

# 넘파이의 배열은 리스트와 달리, 서로 다른 자료형의 값을 원소로 가질 수 없음

'''
배열 vs 리스트
리스트 : 크기가 가변적이고 어떤 원소 타입도 저장할 수 있음 
         대신 연산시 메모리를 많이 필요로 함
배열 : 같은 타입의 원소만 저장, 메모리를 훨씬 적게 씀
'''

arr = np.arange(10)
# [0 1 2 3 4 5 6 7 8 9]
print('arr =',arr)
print('arr[5] =',arr[5]) # 5
print('arr[5:8] ',arr[5:8]) # [5,6,7]

# 브로드캐스팅. 배열 슬라이스에 스칼라 값을 대입하면, 그 범위에 값이 전파됨
arr[5:8] = 12
print('arr =',arr) # [ 0  1  2  3  4 12 12 12  8  9]

arr_slice = arr[5:8] # address 복사 (값 복사 X / view 역할)
print(arr_slice)

arr_slice[1] = 12345

print(arr) # [    0     1     2     3     4    12 12345    12     8     9]

arr_slice[:] = 64

print(arr) # [ 0  1  2  3  4 64 64 64  8  9]


arr_slice_copy = arr[5:8].copy() # 값 복사
print(arr_slice_copy)  # [64 64 64]
print(arr)             # [ 0  1  2  3  4 64 64 64  8  9]

arr_slice_copy[:] = 8  
print(arr_slice_copy)  # [8 8 8]
print(arr)             # [ 0  1  2  3  4 64 64 64  8  9]

'''
zeros() -> 다 0으로
ones()  -> 다 1로
eye()   -> 대각선만 1로
'''
a2 = np.zeros(3) # 1*3열 1차원 배열 vector 생성   
print(a2) # [ 0 0 0 ] (1x3 행렬)
a3 = np.ones(3) # 1*3열 1차원 배열 vector 생성
print(a3) # [ 1 1 1 ] (1x3 행렬)
a4 = np.arange(1,7,1) # [1 2 3 4 5 6]
print(a4)
k1 = np.eye(3) # identity matrix 단위행렬
print(k1) # 3x3 행렬

z = np.zeros(5)      # zero vector 생성

# 2개의 2차원 배열, 2차원 배열은 3개의 1차원 배열로 구성, 각 1차원 배열의 길이는 4 
o = np.ones([2,3,4]) # one vector 생성 (3차원 배열)
n = np.eye(3)        # identity matrix(단위 행렬) 생성

print(z, '\n',o,'\n',n)
 
# shape() 함수 : 배열의 형태 변환
c = np.array([1,2,3,4]) # flat 1차원
print(c)
print(c.shape) #(4,)
c.shape = (2,2) # 2x2 행렬
print(c)
c.shape = (4,) # 다시 1차원
print(c)

# full() 함수 : 모든 배열의 값을 해당 값으로 채움
b = np.full((2,2),3)
print(b)

a = np.arange(8)
print(a)
# a.shape = (2,4)
# print(a)

# reshape() 배열 변형 : 데이터 크기만 맞으면 원하는 배열로 변형할 수 있음
a = a.reshape(2,4)
print(a)

# random.random() : 0~1사이 임의의 실수값으로 채워진 배열 생성
k = np.random.random((2,2))
print(k)

c = np.arange(1,5)
print(c)  # [ 1 2 3 4 ]
c2 = np.array([1,2,3,4])
print(c2) # [ 1 2 3 4 ]
print(c.ndim) # 1   -> ndim : 차원을 보여줌
print(c.shape) # (4, )    -> 1차원 배열 , 그 길이가 4
# ex) (3, 4) -> 2차원 배열, 첫번째 차원의 크기가 3, 두번째 차원의 크기가 4
# ex) (2, 2, 2) -> 3차원 배열, 첫번째 차원의 크기 2, 두번째 차원의 크기 2, 세번째 차원의 크기 2

c.shape = (2,2) # 4x1 => 2x2 
print(c)
print(c.ndim) # 2
c.shape = (1,4)
print(c) # [[1 2 3 4]]


b = np.full((2,2),3)
print(b)

import random
k = np.random.random((2,2))
print(k)
x = random.random()
print(x) # 스칼라

na = np.array([1,2,3,4,5,6,7,8])
a = na.reshape(2,4)
print(a)
# [[1 2 3 4]
# [5 6 7 8]]

print(a[1,1]) # 1행 1열 요소 -> 값 6
print(a[1][1]) # 1행 1열 요소 -> 값 6

array = np.array([
  [[0,1,2,3],
   [4,5,6,7],
   [8,9,10,11]],
  [[0,1,2,3],
   [4,5,100,7],
   [8,9,10,11]]
])
print(array, array.shape) # array.shsape : (2,3,4)

array = np.array([
  0,1,2,3,4,5,6,7,8,9,10,11,
  0,1,2,3,4,5,100,7,8,9,10,11
])
array1 = array.reshape(2,3,4)
print(array1)
print(array1[1,1,2], array1[1][1][2]) # 100 100

# 4칙 연산
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
# float64 64bit = 64/8 = 8 byte 실수형
# int32 32bit = 32/8 = 4 byte 정수형

print(x+y) # [[ 6.  8.], [10. 12.]]
print(np.add(x,y))

print(x-y)
print(np.subtract(x,y))

print(x*y)
print(np.multiply(x,y))

print(x/y)
print(np.divide(x,y))

v = np.array([9,10])
w = np.array([11,12])

# 벡터의 내적
print(v.dot(w))
print(np.dot(v,w)) # 219

# 행렬과 벡터의 곱
print(x.dot(v))
print(np.dot(x,v)) # [29. 67.]

# 행렬곱
print(x.dot(y))
print(np.dot(x,y))

# 역행렬 구하는 법
A = np.array([[1,2],
             [3,4]])
A_inv = np.linalg.inv(A)
print(A_inv)

a = [1,2,3]
b = [3,4,5]
print(a)
print(b)
print(type(a)) # list
# list 연산 -> 사칙연산 안됨
print(2*a) # [1, 2, 3, 1, 2, 3]
print(a+b) # [1, 2, 3, 3, 4, 5]

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)
print(type(a)) # <class 'numpy.ndarray'>
# np.array 사칙연산 가능
print(2*a) # [2 4 6]
print(a+b) # [5 7 9]

c = np.array([[1,2,3],
             [4,5,6]]) # 2차원 배열 생성
print(c.size) # 6
print(c.shape) # (2,3)

d = np.arange(10).reshape(2,5)
print(d)
print(np.arange(2,3,0.1))
print(np.linspace(1.0,4.0,6))

print(np.zeros((2,2),int))
print(np.zeros((2,2),float))
print(np.ones((2,2))) # 2x2 float 1 행렬
print(np.full((2,2),7)) # 2x2 행렬을 7로 채움
print(np.eye(2)) # identity matrix : 단위행렬
print(np.random.random((2,2)))

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print(a)
print(a[0,0]) # 1
print(a[1,2]) # 7
a[-1,-1] += 10
print(a)
print(a[1,:]) # [5 6 7 8]
print(a[:2,:]) # 0부터 2미만행, 모든 열
print(a[:2,1:3])
print(a[:,0:3:2]) # 모든행, 0부터 3미만 2간격 모든열
print(a[:,-1:-4:-2]) # [[4 2] [8 6] [22 10]]
print(a[:,[3,0,2,1]]) # 모든행, 3,0,2,1열 순서로
print(a[[0,1,2],[0,1,2]]) # [0,0][1,1][2,2]원소 -> [1 6 11]

print(a>5) # a의 원소 중 5보다 큰 것 True로 표시, 아니면 False
print(a[a>5]) # [ 6  7  8  9 10 11 22] : a의 원소 중 5보다 큰 것
b = a[:] # 원본에 영향을 미침 / list는 이렇게 하면 값 복사였음(원본에 영향 X)
# b = a.copy() 값 복사 (원본에 영향 X)
print(b)
b[b%2==0] +=100 # b의 원소 중 짝수인 원소에 100을 더함
print(b)
print(a)

c = np.array([[1,2,3],
              [4,5,6]])
print(c)
d = np.arange(11,17).reshape(2,3)
print(d)

print(c+d) # 원소별 연산
print(c-d) # 원소별 연산
print(c*d) # 원소별 연산
print(c/d) # 원소별 연산
print(c**2)
print(np.sqrt(c)) # 제곱근
print(np.dot(c, d.transpose())) # 행렬 연산
# transpose() : 전치 행렬 -> 주어진 행렬의 행과 열을 서로 바꾼 새로운 행렬
# ex) [[1 2 3] [4 5 6]] -> [[1 4][2 5][3 6]]

print(np.dot(c.T, d)) # c.T : c의 전치행렬

'''
array.var()
: 배열의 분산 계산
  분산은 데이터가 평균값으로부터 퍼져있는 정도를 나타내는 척도
  
array.std()
: 배열의 표준편차
  표준편차는 데이터가 평균값으로부터 퍼져있는 정도를 나타내는 또 다른 척도
'''

# 숫자형 : int32 (정수형 32 비트 -> 정수형의 기본형)
# 실수형 : float64 (실수형 64비트 -> 실수형의 기본형)
ar = np.array([1,2,3.0])
print('자료형 :',ar.dtype)

# 실습 1
# 숫자 15에서 23까지 배열을 만들고 이를 3*3 행렬로 변환하여 출력하라.
array = np.arange(15,24).reshape(3,3)
print(array)

# 실습 2
array = np.arange(1,5)
array1 = np.arange(5,9)
print(array)
print(array1)
# 위의 두 array를 이용해서 아래와 같은 값이 나오도록 코딩하라
# [False False False False]
print(array>array1)

# 실습 3
# 아래와 같이 3학생이 중간고사 점수, 기말고사 점수, 과제점수가 있다.
#           (철수, 영희, 민재)
# 중간고사 = (15, 100, 45)
# 기말고사 = (78,  25, 90)
#     과제 = (81,  45, 99)

m = np.array([15, 100, 45]) 
f = np.array([78, 25, 90])
p = np.array([81, 45, 99])

# 각 중간, 기말, 과제점수의 가중치를 각각 0.4, 0.4, 0.2를 부여하여 가중치의 합을 구하고, 
# 거기에 기타점수 5점을 더하고자 한다.
# 이를 array를 이용해 계산하는 프로그램을 짜 보아라.

score = 0.4* m + 0.4* f + 0.2* p
print(score)
print('철수의 최종점수 :',score[0])
print('영희의 최종점수 :',score[1])
print('민재의 최종점수 :',score[2])

print('중간고사 평균 :',np.mean(m))
print('중간고사 표준편차 :',np.std(m))

