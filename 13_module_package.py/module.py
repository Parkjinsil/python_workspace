'''
모듈 : 함수나 변수 또는 클래스들을 모아 놓은 파이썬 파일(.py)
표준 라이브러리 : 파이썬에 내장된 모듈들
패키지 : 모듈과 패키지들의 구조화된 collection

파이썬 모듈 : 함수,변수,상수 및 클래스를 모두 모아놓은 파일 
             하나의 파일을 의미, 모듈이름 = 파일이름
'''
import mycircle
import myrect
import mysquare
import run
import test_package.say_goodbye

# area = mycircle.get_peri(5)
# print('반지름 10의 원의 면적 :',area)

# area2 = myrect.get_area(5,4)
# print('가로 5 세로 4인 사각형의 면적은',area2)

# # 모듈의 문서화 __doc__ 속성
# area3 = mysquare.get_area(20)
# print(mysquare.__doc__)
# print(mysquare.get_area.__doc__)

# run.openurl('naver.com')
# # 5! = 1x2x3x4x5
# # degree 각도 radian 라디안
# # 차트 로그 차트로 그려야 할 수 있음
# from mycircle import get_area
# # area = get_area(20)
# # print(area)
    
# import modl
# print(modl.sum(3,4))

# print(modl.safe_sum(3,4))

# print(modl.safe_sum(1,'a'))

# from modl import sum, safe_sum

# print(sum(3,4))
# print(safe_sum(3,4))
# print(safe_sum(1,'a'))

# import test_package.say_hello, test_package.say_goodbye
# test_package.say_hello.hello()
# test_package.say_goodbye.goodbye()

# from test_package import say_hello
# from test_package import say_goodbye
# say_hello.hello()
# say_goodbye.goodbye()

# import mod2
# print(mod2.PI)
# a = mod2.Math()
# print(a.solv(2))
# print(mod2.sum(mod2.PI,4.4))

# import sys
# sys.path.append('c:/doit')

# import mylib
# mylib.myprint()

# from mymod import mysum
# mysum(1,2)

import numpy as np
x = np.arange(15, dtype=np.int64).reshape(3,5) # 3행 x 5열 배열로 바꾼다
print(x)

x[1:, ::2] = -99
# 1 -> 두번째 행부터 전체 행 의미
# ::2 -> 열 방향으로 2칸씩 건너뛰면서 선택한다는 의미
# 이 원소들을 다 -99로 바꿈
# [[  0   1   2   3   4]
# [-99   6 -99   8 -99]
# [-99  11 -99  13 -99]]

print(x)
x.max(axis=1) 
# axis=1 은 행 방향으로 최대값을 구한다는 의미
# 결과적으로 각 행의 최대값으로 이루어진 1차원 배열 반환 됨
# [4, 9, 14]

import sympy as sp
# pip install sympy
# 변수 선언
x = sp.symbols('x')
# 2차 방정식 정의
equation = x**2 -4*x + 3
roots = sp.solve(equation,x)
print(roots) # [1,3]

