import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = 'https://github.com/dongupak/DataML/raw/main/csv/'
weather_file = path + 'weather.csv'

weather = pd.read_csv(weather_file, index_col=0, encoding='CP949')
# index_col=0 : CSV 파일을 읽어올 때 첫 번째 열을 데이터프레임의 인덱스로 사용하겠다는 뜻
# encoding = 'CP949'는 한글 인코딩 방식 
print(weather.head(3))
# 전체 테이블의 크기
print('weather 데이터의 shape :',weather.shape)

print(weather.describe())

# 데이터 정제 : 데이터를 처리하기 전에 반드시 거쳐야 하는 절차

# 개별적인 열의 개수
print(weather.count())

# 결손값 : 항목이 비어있는 것 -> isna()로 탐지
missing_data = weather[weather['평균풍속'].isna()]
print(missing_data)

# 결손값을 다루는 방법 
# : 결손값을 가진 행이나 열 전체를 삭제하는 것 (가장 간단)
# : 결손값을 다른 값으로 교체 -> fillna()
#   -> 결손값을 단순히 0으로 채우게 되면 데이터의 개수가 적을 경우 전체 데이터의 대표값인 평균값을 왜곡할 수 있음

weather.fillna(weather['평균풍속'].mean(), inplace=True)
print(weather.loc['2012-02-11'])

'''
사계열 데이터 (time series) 란?
: 시간의 흐름에 따라 순차적으로 관측한 값들의 집합
'''

# 다양한 형식의 연, 월, 일 표시 데이터
d_list = ['01/03/2018','01-03-2018','2018/01/05', '2018/01/06']
print(pd.DatetimeIndex(d_list).year)  # 년도 값을 출력함
print(pd.DatetimeIndex(d_list).month) # 월 값을 출력함
print(pd.DatetimeIndex(d_list).day)   # 일 값을 출력함

dt_list = ['01,03,2018 11:12:13', '01-03-2018 11:22:13']
print(pd.DatetimeIndex(dt_list).hour) # 시 값을 출력함
print(pd.DatetimeIndex(dt_list).minute) # 분 값을 출력함

# '일시'라는 이름의 열을 사용하여 연도와 달,날을 얻기 위해 사용하는 방법
weather = pd.read_csv(weather_file, encoding='CP949')
# weather['일시'] = pd.DatetimeIndex(weather['일시']).year
print(weather)

# # 그래프로 그려보기
weather['month'] = pd.DatetimeIndex(weather['일시']).month
print(weather)

monthly = [None for x in range(12) ] # 달별로 구분된 12개의 None 값
monthly_wind = [ 0 for x in range(12) ] # 각 달의 풍속을 담을 리스트
for i in range(12):
    monthly[i] = weather[weather['month'] == i+1 ] # 달별로 분리
    # weather['month'] == i+1 : 데이터 프레임에서 'month' 열의 값이 i+1인 행들을 선택
    # weather[weather['month'] == i+1] : i+1월의 데이터를 포함하는 새로운 데이터프레임을 만듦
    # 이 새로운 데이터프레임을 monthly[i]에 저장
    monthly_wind[i] = monthly[i]['평균기온'].mean() # 개별 데이터 분석
    # monthly[i]['평균기온']은 monthly[i] 데이터프레임에서 '평균기온'열만 선택함
    # 평균 값을 계산해서 monthly_wind[i]에 저장함
    
months = np.arange(1,13)  # 1에서 12월의 연속된 수를 생성
plt.bar(months, monthly_wind, color='green')
plt.xlabel('Month')
plt.ylabel('Temperature')
# plt.show()

# 'month'열에 대하여  groupby() 적용해서 보기
weather1 = weather.drop('일시', axis=1)
monthly_means = weather1.groupby('month').mean()
# print(monthly_means)

# 'year'만들고 groupby()해서 보자
# weather['year'] = pd.DatetimeIndex(weather['일시']).year
# weather1 = weather.drop('일시', axis=1)
# yearly_means = weather1.groupby('year').mean()
# print(yearly_means)

# 특정 조건을 만족하는 데이터만을 추출하는 방식
print(monthly_means['평균풍속']>=4.0)

'''
pivot()
: 테이블의 구조 변경하는 pandas 대표 메소드
'''
df = pd.DataFrame({'상품':['시계','반지','반지','목걸이','팔찌'],
                   '재질':['금','은','백금','금','은'],
                   '가격':[500000, 20000,350000,400000,60000]})
print(df)

# pivot() 이용해서 index='상품'으로 바꾸기
new_df = df.pivot(index='상품',columns='재질',values='가격')
new_df = new_df.fillna(value=0)
print(new_df)

# 테이블 데이터 결합 : concat() / merge()
df_1 = pd.DataFrame({'A':['a10','a11','a12'],
                     'B':['b10','b11','b12'],
                     'C':['c10','c11','c12']},
                    index=['가','나','다'])
df_2 = pd.DataFrame({'B':['b23','b24','b25'],
                     'C':['c23','c24','c25'],
                     'D':['d23','d24','d25'],},
                    index=['다','라','마'])

# concat() 함수는 디폴트로 행을 늘려 테이블 늘려감
df_3 = pd.concat([df_1,df_2])
print(df_3)

# joi='inner'로 하면 교집합인 B,C열만 남음
df_4 = pd.concat([df_1,df_2], join='inner')
print(df_4)