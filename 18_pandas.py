'''
Pandas 
: Python에서 빅데이터 분석을 다루기 위한 라이브러리
: 판다스는 넘파이를 기반으로 하기 때문에 처리속도가 빠르고, 
  행과 열로 잘 구조화된 데이터프레임을 제공하며, 이 데이터프레임을 조작할 수 있는 다양한 함수를 지원한다.

Pandas로 할 수 있는것
- 파이썬 리스트, 딕셔너리, 넘파이 배열을 데이터프레임으로 변환 가능
- CSV, TSV 파일이나, 엑셀 파일 등을 열 수 있음
- URL을 통해 웹 사이트의 CSV / JSON과 같은 원격 파일 / 데이터베이스 열 수 있음  
  
Numpy의 한계
: 2차원 행렬 데이터는 모두 같은 자료값을 가지는 단순한 수치 정보 중심으로만 구성되어 있음

1차원 데이터 vs 2차원 데이터
: 1차원 데이터 -> 하나의 컬럼(열) 가지고 있는 데이터
  2차원 데이터 -> 두 개 이상의 컬럼(열) 가지고 있는 데이터, DataFrame의 객체로 표현됨
'''
import numpy as np
import pandas as pd

'''
Series는 1차원 배열과 유사한 자료구조 but 값(value)들에 인덱스 레이블이 자동으로 붙음
'''
se = pd.Series([1,2,np.nan,4]) # np.nan : 결측값
print(se)

# isna() -> 결손값(결측값: NULL)이 있는지 boolean으로 반환하는 함수

data = [1,2,np.nan,4]
indexed_se = pd.Series(data, index = ['a','b','c','d'])
print(indexed_se)

indexed_se['a'], indexed_se['b'] # 인덱스가 'a','b',...임

income = {'1월':9500, '2월':6200, '3월':6050, '4월':7000}
income_se = pd.Series(income) # 월을 인덱스로 하는 매출 시리즈
print('동윤이네 상점의 수익')
print(income_se)

from pandas import Series, DataFrame
k = Series([100, 101, 102, 103, 104, 105])
print(k)
print(k[0])
print(k[1])
print(k[5])

k1 = Series([100,101,102,103,104,105],index=['2018-11-01','2018-11-02','2018-11-03','2018-11-04','2018-11-05','2018-11-06'])
print(k1)

# Series의 index와 values를 통해 원하는 값에 접근 가능
for date in k1.index:
    print(date)
    
for money in k1.values:
    print(money)

# Series의 브로드캐스트 기능 - 인덱스가 달라도 연산가능 
# 브로드캐스트 : 서로다른 형상(shape)의 배열 간에도 연산 가능 
mine = Series([10,20,30],index=['korean', 'english', 'math'])
friend = Series([70,50,50],index=['korean','english','math'])

merge = mine + friend
print(merge)

mine = Series([10,20,30],index=['naver', 'sk', 'kt'])
friend = Series([10,30,20],index=['kt','naver','sk'])

merge = mine + friend
print(merge)

'''
DataFrame
: 여러 개의 column으로 구성된 2차원 형태의 자료 구조 처리
: 2차원 형태의 표(행/열) 구조를 가지는 자료 구조
  행과 열에 대한 인덱스를 가지고 순서대로 배열됨
  열 1개가 하나의 Series 구조 (axis=0(기본값): 행으로 분리 , axis=1: 열로 분리)

DataFrame() 인자
-> data : 데이터프레임의 데이터로 딕셔너리, 리스트, 넘파이 배열 등을 전달 할 수 있음
   index : 행 인덱스(row index)를 지정함
   columns : 열 이름(column names)을 지정
   dtype : 데이터 타입 지정
'''
# 다양한 데이터타입으로 생성 가능
nparray1 = np.array([[1,2,3],[4,5,6]]) # numpy array
dp = pd.DataFrame(nparray1)
print(dp)

dictionary1 = {'a':['1','3'],'b':['1','2'],'c':['2','4']} # dictionary
dp = pd.DataFrame(dictionary1)
print(dp)

# 딕셔너리로부터 DataFrame 생성 예
raw_data = {'col0':[1,2,3,4],
            'col1':[10,20,30,40],
            'col2':[100,200,300,400]}
data = DataFrame(raw_data)
print(data)

print(data['col1'])

# 행의 index 및 columns 키워드 지정하기
daeshin = {'open':[11650,11100,11200,11100,11000],
           'high':[12100,11800,11200,11100,11150],
           'low':[11600,11050,10900,10950,10900],
           'close':[11900,11600,11000,11100,11050]}
daeshin_day = DataFrame(daeshin)
print(daeshin_day)

# 행의 index 및 columns 키워드 지정하기
date = ['16.02.29','16.02.26','16.02.25','16.02.24','16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open','high','low','close'],index=date)
print(daeshin_day.columns)
print(daeshin_day.index)
print(daeshin_day)

# column 선택 : df['컬럼명']
close = daeshin_day['close']
print(close)

# 행(row) 선택 : df.loc['인덱스']
# print(daeshin_day['16.02.24']) -> '16.02.04' 이 값을 컬럼의 키 값으로 판단함
#                                    그러나 daeshin_dayd라는 DataFrame 객체에는 '16.02.04'라는 키 값을 갖는 칼럼이 없으므로 에러 발생
# 이럴 땐 loc, iloc 메소드 사용
# loc : 명칭 기반 인덱싱 (레이블 인덱싱)
# iloc : 위치 기반 인덱싱 (정수 인덱싱)
# ** df.loc[0:2] : 0 에서 2 까지
#    df.iloc[0:2] : 0 에서 1 까지
day_data = daeshin_day.loc['16.02.24']
print(day_data)

dataframe1 = pd.DataFrame(data=[4,5,6,7],index=range(0,4), columns=['A'])
dp = pd.DataFrame(dataframe1) 
print(dp)

series1 = pd.Series({'United Kingdom':'London', 'India':'New Delhi', 'United States':'Washington',
                    'Belgium':'Brussels'}) # Series는 Pandas의 벡터 데이터형
dp = pd.DataFrame(series1)
print(dp)

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=[10,11,12])
print(df)
print(len(df)) # 3 df의 data 개수(index(행) 기준)
print(df.columns)
df.columns = ['A','B','C'] # df 컬럼명 변경
print(df)
print(df['A']) # 컬럼 선택
print(df[['A','B']]) # 다중컬럼 선택
print(df['B'][0:2]) # 'B' 컬럼 중 0~1 index 선택
print(df.iloc[0]) # index 0 선택
print(df.iloc[0:2]) # index 0 ~ 1 선택
print(df.iloc[0:2]['B']) # 'B' 컬럼 중 index 0~1 선택

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]])) # df 생성
print(df)
# 행 추가 (df.iloc은 새로운 행을 추가할 때 사용 X)
df.loc[3] = [10,11,12]
print(df)
# 마지막 행에 행데이터 추가
# ignore_index=False의 경우 index는 0으로 세팅
df = df._append([[10,11,12]],ignore_index=True)
print(df)

df.columns = list('ABC') # 컬럼면 변경
df['D'] = list('ddddd') # 컬럼명으로 추가
print(df)

df[4] = [4]*5 # 컬럼명으로 추가
print(df)
df[7] = [7]*5 # 컬럼명으로 추가
print(df)

# 삭제
df = df.drop(7, axis=1) # 컬럼 삭제
print(df)
df = df.drop([4,'D'], axis=1) # 다중컬럼 삭제
print(df)
df = df.drop(4, axis=0) # 행 삭제
print(df)
df = df.drop([2,3], axis=0) # 다중행 삭제
print(df)

# 데이터 변경
df.loc[0][0] = 100 # label 기준(불일치시 index 기준) 변경
print(df)
df.loc[0]['B'] = 100
print(df)
df.iloc[1][1] = 100 # index 기준(불일치시 label 기준) 변경
print(df)          
df.iloc[1]['C'] = 100
print(df)
df.iloc[0][0:2] = [1,2] # 다중데이터 변경
print(df)
df['C'] = [3,6] # 컬럼 변경
print(df)

# df 생성
df = pd.DataFrame({'cluster':[1,1,2,1,2,3],'org':['a','a','h','c','d','w'],
                   'time':[8,6,34,23,74,6]})
print(df)
# 'time' 기준으로 역순으로 정렬
df = df.sort_values(['time'], ascending=[False]) # 'time'기준으로 역순으로 정렬
print(df)
df = df.reset_index(drop=True) # index 정리
print(df)

# 함수
# df 생성
df = pd.DataFrame({'cluter':[1,1,2,1,2,3],'org':['a','a','h','c','d','w'],
                  'time':[8,6,34,23,74,6]})
print(df)
# 기초 통계량
print(df.describe())
# 데이터 head 부분만 보여줌
print(df.head(2))
# 데이터 tail부분만 보여줌
print(df.tail(2))
# transpose : 행과 열 바꿔서 보여줌
print(df.T)
# 'time' 컬럼 데이터
print(df['time'])
print(df.time) 
# 'time'이 10 미만인 데이터
print(df[df.time<10])

month_se = pd.Series(['1월','2월','3월','4월'])
income_se = pd.Series([9500,6200,6050,7000])
expenses_se = pd.Series([5040,2350,2300,4800])
df = pd.DataFrame({'월':month_se,'수익':income_se,'지출':expenses_se})
print(df)

# 판다스 Series를 이용하여 최대 수익 월을 출력하기
m_idx = np.argmax(income_se) # 넘파이의 argmax() 사용 : 최대값의 위치(인덱스) 알려줌
print('m_idx :',m_idx)
print('최대 수익이 발생한 월 :',month_se[m_idx])
print('월 최대 수익 :',income_se.max(),', 월 평균 수익 :',income_se.mean())

# 도전문제 6 (난이도 중)
print('동윤이네 상점의 수입 합계 :{:,}'.format(sum(df['수익'])))
print('동윤이네 상점읭 지출 합계 :{:,}'.format(sum(df['지출'])))

'''
* 데이터프레임의 컬럼값과 인덱스값을 출력하려면
   df.columns  ->  컬럼값들
   df.index    ->  인덱스값들
   
* df.columns.toList() : 데이터프레임의 컬럼들을 리스트형으로 반환
* df['2007'].toList() : 2007년도 컬럼들의 값들을 리스트형으로 반환

* 모든 값들의 합 
 : df['2007'] + df['2008'] + df['2009'] + df['2010'] + df['2011']
  => df.sum(axis=1) : 열 방향으로(행의 합)
     df.sum(axis=0) : 행 방향으로(열의 합)
'''
# data = [[7.71, 7.95, 11.96, 15.84, 16.33],
#         [19.02, 17.71, 15.00, 16.70, 17.48],
#         [10.47, 8.45, 5.58, 7.60, 8.40],
#         [10.87, 10.83, 7.55, 9.09, 7.88],
#         [4.04, 3.78, 3.45, 4.20, 4.62],
#         [2.01, 2.05, 1.50, 2.25, 2.54]]
# df = DataFrame(data, columns=['2007','2008','2009','2010','2011'],
#                index=['China','EU','US','Japan','Korea','Mexico'])
# print(df)
# df['total'] = df.sum(axis=1)
# df['mean'] = df[['2007','2008','2009','2010','2011']].mean(axis=1)
# print(df)

# df.drop('2007', inplace=True, axis=1) # inplace=True : 새 객체 반환 X , 기존 객체 직접 수정
# print(df) # 이전에 구한 total, mean 값이 나타남
# # 2008부터 2011년도까지의 총생산 수와 평균을 다시 계산함
# df['total'] = df[['2008','2009','2010','2011']].sum(axis=1)
# df['total'] = df.sum(axis=1)
# df['mean'] = df.mean(axis=1)
# print(df)

# 도전문제 6.2 (난이도 상)
# df.loc['Total'] = df.loc[['China','EU','US','Japan','Korea','Mexico']].sum(axis=0)
# df.loc['Total'] = df.sum(axis=0)
# print(df)

# d_df = pd.DataFrame(data=[[10,20,30,40],[50,60,70,80]],
#                     columns = ['A','B','C','D'])
# new_df = d_df.drop('B', axis=1, inplace=False)
# print(new_df) # 'B'열이 삭제된 새로운 데이터프레임
# print(d_df) # d_df 데이터프레임은 변화가 없음

path = 'https://github.com/dongupak/DataML/raw/main/csv/'
file = path+'vehicle_prod.csv'
df = pd.read_csv(file, index_col=0) # 원격지에 접속하여 csv를 읽어옴
print(df)

df.drop('Mexico',axis=0,inplace=True) # Mexico 행을 삭제하고 df를 갱신
print(df)

df = pd.read_csv(file, index_col=0)
print(df.head(3))

print(df[2:6]) # 지정된 범위의 레코드 가져옴
print(df.loc['Korea']) 
print(df.loc[['US','Korea']])

# 열 선택과 행 선택을 결합하는 방법
print(df['2011'][[0,4]])
print(df['2011'][['China','Korea']]) # 위와 같음
# 보다 상세하게 특정한 요소 하나 선택
print(df.loc['Korea','2011'])
