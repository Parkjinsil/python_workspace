from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# IRIS 데이터셋 로드
iris = load_iris()

# 특성과 타겟 데이터 분할
X = iris.data
y = iris.target

# 학습 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

# KNN 모델 초기화 및 파라미터 설정
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', n_jobs=1)

# 모델 학습
knn.fit(X_train, y_train)

# 분류 결과 예측
y_pred = knn.predict(X_test)

# 분류 결과 평가
report = classification_report(y_test, y_pred)
print(report)

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# 탐색할 파라미터 그리드 정의
param_grid = {
    'n_neighbors' : [1,3,5], # 이웃의 수
    'weights' : ['uniform','distance'],
    'algorithm' : ['ball_tree', 'kd_tree', 'brute'] # 가중치 함수
}

# GridSearchCV를 사용하여 최적 파라미터 탐색
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(X, y)

# 최적 파라미터 확인
best_params = grid_search.best_params_
print('Best Parameters :',best_params)

# 최적 파라미터로 훈련된 모델 사용하여 예측
y_pred = grid_search.predict(X_test)

# 분류 결과 평가
report = classification_report(y_test, y_pred)
print('Classification Report :')
print(report)

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# Breast Cancer 데이터셋 로드
breast_cancer = load_breast_cancer()

# 특성 데이터와 타겟 데이터
X = breast_cancer.data
y = breast_cancer.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN 모델 초기화
knn = KNeighborsClassifier(n_neighbors=5,
                           weights='uniform',
                           algorithm='auto',
                           leaf_size=30,
                           p=2,             # 유클리디언 거리
                           metric='minkowski',
                           n_jobs=None)

# 모델 학습
knn.fit(X_train, y_train)

# 분류 결과 예측
y_pred = knn.predict(X_test)

# 평가 리포트 출력
report = classification_report(y_test, y_pred)
print(report)
                 
                 
# 탐색할 파라미터 그리드 정의
param_grid = {
    'n_neighbors' : [3,5,7],  # 이웃의 수
    'weights' : ['uniform', 'distance'],
    'algorithm' : ['ball_tree', 'kd_tree', 'brute'] # 가중치 함수
}                               

# GridSearchCV를 사용하여 최적 파라미터 탐색
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(X, y)

# 최적 파라미터 확인
best_params = grid_search.best_params_
print('Best Parameters :', best_params)

# 최적 파라미터로 훈련된 모델 사용하여 예측
y_pred = grid_search.predict(X_test)

# 분류 결과 평가
report = classification_report(y_test, y_pred)
print('Classification Report :')
print(report)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# 데이터 로드
wine = load_wine()

print(wine)

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = pd.Series(wine.target)

# 데이터셋 정보 출력
print(df.info())
df.head()

# 데이터셋 요약 통계량 출력
print(df.describe())

# 각 피처의 분포 확인
df.hist(bins=30, figsize=(15, 10))
plt.show()

# 피처 간 상관관계 시각화
sns.pairplot(df, hue = 'target')
plt.show()

# 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(wine.data,
                                                    wine.target,
                                                    test_size=0.3,
                                                    random_state=42)

# KNN 모델 학습 및 예측
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform',
                           algorithm='auto', leaf_size=30,
                           p=2, metric='minkowski')
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# 분류 결과 평가
report = classification_report(y_test, y_pred)
print(report)

from sklearn.model_selection import GridSearchCV

# 탐색할 파라미터 범위
param_grid = {
    'n_neighbors':[3,5,7],
    'weights':['uniform','distance'],
    'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute']
}

# 그리드 서치 수행
grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# 최적 파라미터 출력
print('Best parameters :',grid_search.best_params_)

# 최적 파라미터로 훈련된 모델 사용하여 예측
y_pred = grid_search.predict(X_test)

# 분류 결과 평가
print('Classfication Report :')
print(report)
