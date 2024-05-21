import matplotlib.pylab as plt
import numpy as np

# plt.plot([1,2,3,4]) # = plt.plot([0,1,2,3],[1,2,3,4])
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('my xy graph')
# plt.show()

# x = np.arange(10)
# plt.plot(x**2)
# plt.show()

# x = np.arange(10)
# plt.plot(x**2)
# plt.axis([0,100,0,100]) # 범위를 지정함
# plt.show()

# x = np.arange(-20,20) # -20에서 20 사이의 수를 1의 간격으로 생성
# y1 = 2*x 
# y2 = (1/3)*x**2+5
# y3 = -x**2-5
# # 녹색 점선 원기호와,빨간색 실선 세모기호, 파랑색 별표와 점선으로 함수를 표현
# plt.plot(x,y1,'go-',x,y2,'r^-',x,y3,'b*:')
# plt.axis([-30,30,-30,30]) # 그림 그릴 영역 지정함
# plt.show()

# N = 50
# x = np.arange(N)
# y = np.random.random(size=N)

# plt.plot(x,y,'g^:') # 녹색 점선 세모표시
# plt.show()

from IPython.display import Image

# x = np.linspace(0,np.pi*2, 100) # start에서 stop 까지 균등한 간격으로 step개 숫자 생성
# fig = plt.figure()
# plt.plot(x,np.sin(x), 'r-') # 사인함수는 빨간 실선
# plt.plot(x,np.cos(x),'b:')  # 코사인함수는 파란 점선
# fig.savefig('sin_cos_fig.png')
# # Image('sin_cos_fig.png') # Jupyter Notebook이나 JupyterLab과 같은 노틉툭 환경에서만 이미지 출력 실행됨
# plt.show() # 일반 Python 스크립트나 REPL 환경에서는 Image 함수가 작동하지 않으므로 plt.show() 해야지만 출력됨

# plt.style.use('dark_background')
x = np.linspace(0,np.pi*2, 100)

# plt.title('Sin cos curve')
# plt.rc('font',family='Malgun Gothic') # 한글로 제목 가능
# plt.title('사인 코사인 커브') 
# plt.plot(x, np.sin(x),'r-',label = 'sin curve', c = 'yellow') # 컬러 지정도 가능
# plt.plot(x, np.cos(x), 'b:', label = 'cos curve')
# plt.xlabel('x value') # x축에 이름 붙이기
# plt.ylabel('y value')
# # plt.legend() # -> 범례 표시 label을 plot에 넣어줘야 표시됨
# plt.legend(loc='upper right') # 위쪽 오른편에 범례 표시
# plt.show()

# t = np.arange(0,10,2) 
# plt.plot(t,t) # plt를 여러번 호출해서 함수를 여러 개 그릴 수 있음
# plt.plot(t,t**2)
# plt.plot(t,t**3)

# # plt.plot(t,t, t,t**2, t, t**3) # 이렇게 한번에 쓸 수도 있음

# plt.xlabel('x datas')
# plt.ylabel('y datas')
# plt.grid() # 이렇게 눈금 칸을 이용해서 더 확실하게 살펴볼 수 있음
# plt.show()

# plt.scatter(3,5) # (3,5)좌표에 점 찍기
# plt.title('practice scatter function', fontsize=15)
# plt.show()

# x = np.arange(0,10,1)
# plt.scatter(x, x**2, c = 'k', s = 10) # s를 이용해서 점의 크기를 변경할 수 있음
# plt.text(3,50,'y=x^2 graph') # 임의로 원하는 좌표에 텍스트 추가하기
# plt.show()

'''
* 선의 종류
디폴트가 직선, 점으로 표현하는 마커나 점선 선택 가능
선의 선택은 plot에서 세번째 인자 -> 선의 종류
                    네번째 인자 -> 색 지정
                    
* 타이틀 : plt.title('타이틀명')
* X축 라벨 : plt.xlabel('X축 라벨명')
* Y축 라벨 : plt.ylabel('y축 라벨명')

* 구간 확대/축소
: 그래프는 입력되는 x,y의 최소,최대 구간으로 자동으로 그려짐
  이 구간 키우거나 줄이려면 -> x축 : plt.xlim(최소, 최대)
                             y축 : plt.ylim(최소, 최대)
                             
* 레전드
: 그래프를 그릴 때 여러개의 그래프를 같익 그릴 수 있는데, 이 경우 각 그래프가 구분이 안됨
 -> 그래프마다 라벨을 달 수 있음 plt.legend('위치')
 
* 어노테이션
: 그래프에 화살표를 그린 후, 그 화살표에 문자열을 출력하는 기능
  ex) plt.annotate('문자열',xy,xytext,arrowprops)
     : xy -> 화살표가 가르키는 점의 위치
       xytext -> 문자열이 출력될 위치
       arrowprops -> 화살표의 속성으로 칼라등을 정의
'''
# x = np.arange(1,10)
# y = x*5

# plt.plot(x,y)
# plt.annotate('annotate',xy=(2,10),xytext=(5,20),arrowprops={'color':'green'})
# plt.show()

# 스타일 지정
# plt.plot([10,20,30,40],[1,4,9,16],'rs--')
# plt.show()

# plt.plot([10,20,30,40],[1,4,9,16],c='b', lw=5,ls='--',marker='o',ms=15,mec='g',mew=5,mfc='r')
# plt.show()

# titleFont = {'fontsize': 20, 'color':'#0000ff'}

# plt.subplot(211).set(xticks=[-4,-2,0,2,4], yticks=[-1,0,1])
# # 211 -> 2행 1열의 첫번째 그래프
# triXAxis = np.linspace(-4,4,100)
# sinYAxis = np.sin(triXAxis)
# cosYAxis = np.cos(triXAxis)
# plt.plot(triXAxis, sinYAxis, label = "Sin Funtion", linestyle='--')
# plt.plot(triXAxis, cosYAxis, label = "Cos Function", linestyle='-.')
# plt.legend()
# # plt.title('Trigonometric Functions', fontdict=titleFont)

# # 축의 간격 설정 : plt.xticks(), plt.yticks()
# #                -> list 형으로 넣고싶은 눈금의 숫자를 입력해줘야 함
# # plt.xticks([-4,-2,0,2,4])  -> plt.subplot().set()함수로 간단하게 쓸 수 있음
# # plt.yticks([1,0,-1])
# plt.title('Trigonometric Functions', loc = 'right') # loc 매개변수는 제목을 정렬해주는 변수

# plt.subplot(212).set(xlim=[0,8],ylim=[0,3])
# # 212 -> 2행 1열의 두번째 그래프
# logXAxis = np.linspace(1,10,100)
# logYAxis = np.log(logXAxis)
# plt.plot(logXAxis, logYAxis)
# plt.title('log Function')
# plt.show()

'''
* 다양한 종류의 그래프를 한 화면에 여러개 그리기에 편리 -> subplots() 함수
 : subplots() 함수는 figure 객체(컨테이너 객체)와 Axes 객체(그림 그릴 수 있는 테두리 상자 모양)를 반환함

fig, ax = matplotlib.pyplot.subplots( nrows = 2, ncols = 2, ...)
-> fig : 그리기 요소들을 포함하는 컨테이너 (여러 개의 Axes를 가질 수 있음)
   ax  : 그림을 그릴 수 있는 공간 Axes (Axes 객체)    !=    Axis 객체 : x축, y축
   mayplotlib.pyplot : 필요한 모듈
   nrows : 행의 수
   ncols : 열의 수
'''

# fig, ax = plt.subplots(2,2) # 2행 2열의 그림을 그리는 공간을 만든다

# X = np.random.randn(100) # 정규 분포를 가지는 데이터
# Y = np.random.randn(100) # 정규 분포를 가지는 데이터
# ax[0,0].scatter(X,Y)     # 산점도 그림
# X = np.arange(10)
# Y = np.random.uniform(1,10,10) # 균일 분포값 생성
# ax[0,1].bar(X,Y)         # 막대 차트 그림
# X = np.linspace(0,10,100)
# Y = np.cos(X)
# ax[1,0].plot(X,Y)        # 실선으로 함수를 그림
# Z = np.random.uniform(0,1,(5,5))
# ax[1,1].imshow(Z)        # 분포를 2D 이미지로 그림
# plt.show()

# subplots로 12개 그리기
# fig, axes = plt.subplots(3,4)
# axes[1,2].plot([1,2,3,4]) # subplots으로 반환한 axes는 배열처럼 접근 가능
# axes[2,1].plot([1,2,3,4],[1,2,3,4])
# plt.tight_layout() # subplot간 margin이 겹치지 않게 하는 함수
# plt.show()

# fig, ax = plt.subplots(1,2) # 1행 2열
# fig.suptitle('figure title')
# ax[0].set_title('ax[0] title')
# ax[1].set_title('ax[1] title')
# plt.tight_layout()
# plt.show()

# subplot으로 다른 크기 그리기
# ax221 = plt.subplot(2,2,1)
# ax222 = plt.subplot(2,2,2)
# ax212 = plt.subplot(2,1,2)

# ax221.scatter([1,2,3],[3,2,1])
# ax212.plot([1,2,3,4,5]) # subplot으로 만든 ax는 각각을 개별적으로 사용할 수 있음

# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,8))
# plt.subplot(3,2,1)
# plt.subplot(3,2,3)
# plt.subplot(3,2,5)
# plt.subplot(2,2,2)
# plt.subplot(2,2,4)
# plt.show()

# plt.subplot(221)
# triXAxis = np.linspace(-4,4,100)
# sinYAxis = np.sin(triXAxis)
# cosYAxis = np.cos(triXAxis)
# plt.plot(triXAxis,sinYAxis)
# plt.plot(triXAxis,cosYAxis)

# plt.subplot(223)
# logXAxis = np.linspace(1,10,100)
# logYAxis = np.log(logXAxis)
# plt.plot(logXAxis, logYAxis)

# plt.subplot(122)
# quadXAxis = np.linspace(-10,10,100)
# quadYAxis = quadXAxis**2
# plt.plot(quadXAxis, quadYAxis)

# plt.show()

# fig, ax = plt.subplots(2,3)
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.3, 0.5, str((i,j)),fontsize=11) # 텍스트만 표시
# plt.tight_layout()
# plt.show()

# Grid로 나누기
# grid = plt.GridSpec(2,3,wspace=0.4, hspace=0.3)

# X = np.random.randn(100)
# Y = np.random.randn(100)
# plt.subplot(grid[0,0]).scatter(X,Y)

# X = np.arange(10) # 정규 분포를 가지는 데이터
# Y = np.random.uniform(1,10,10)
# plt.subplot(grid[0,1:]).bar(X,Y)

# X = np.linspace(0,10,100)
# Y = np.cos(X)
# plt.subplot(grid[1, :2]).plot(X,Y)

# Z = np.random.uniform(0,1,(5,5))
# plt.subplot(grid[1,2]).imshow(Z)

# plt.show()

# grid = plt.GridSpec(3,3, wspace = 0.4, hspace=0.3)

# X = np.random.randn(100)
# Y = np.random.randn(100)
# plt.subplot(grid[0,:]).scatter(X,Y)

# X = np.arange(1.0,4.0)
# Y = X
# plt.subplot(grid[1,0:2]).plot(X,Y,'r--')

# Z = np.random.uniform(0,5,(10,5))
# plt.subplot(grid[1:,2]).imshow(Z)

# X = np.linspace(0,10,100)
# Y = np.cos(X)
# plt.subplot(grid[2,0]).plot(X,Y,'g-')

# X = np.arange(10)
# Y = np.random.uniform(1,10,10)
# plt.subplot(grid[2,1]).bar(X,Y)

# plt.show()

'''
np.linspace() vs np.random.uniform()
: linspace()는 특정 범위 내에서 균등한 간격으로 숫자를 생성
  uniform()은 특정 범위 내에서 균등분포를 따르는 임의의 난수(불규칙적이고 예측 불가능한 수)를 생성 (random과 같이 사용해야함)
  -> linspace()는 주로 그래프 축이나 범위를 정의할 때 사용
     uniform()은 실험이나 시뮬레이션에서 난수가 필요할 때 사용
     
  ex) x = linspace(0,10,5) 
      random_nums = np.random.uniform(0,1,5)  : 0 과 1 사이의 5개의 난수
'''

# x = np.arange(1,10)
# y1 = x*5
# y2 = x*1
# y3 = x*0.3
# y4 = x*0.2

# plt.subplot(1,2,1)
# plt.plot(x,y1)
# plt.subplot(1,2,2)
# plt.plot(x,y2)
# plt.show()

# 제주도 데이터 문제
'''
barh 함수 : 가로 방향의 바 차트 그리는데 사용

plt.barh(x, height, height=0.8, left=None, **kwargs)
-> x : 바의 x좌표 값을 나타내는 배열 또는 숫자
   height : 바의 높이를 나타내는 배열 또는 숫자
   height : 바의 상대적인 높이(0과 1 사이의 값, 기본값은 0.8)
   left : 바의 왼쪽 가장자리 x좌표 값(기본값은 None)
   **kwargs : 색상, 에지, 색상, 라벨 등의 옵션 매개변수
'''
y = np.arange(3)
years = ['2010','2011','2012']
domestic = [6801, 7695, 8010]
foreign = [777, 1046, 1681]

plt.barh(y, domestic)
plt.barh(y, foreign)
plt.yticks(y, years)
plt.show()
