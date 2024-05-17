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

