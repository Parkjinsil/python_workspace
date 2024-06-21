from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# 캘리포니아 집값 데이터셋 로드
california_housing = fetch_california_housing(as_frame=True)

# 특성 데이터와 타겟 데이터
X = california_housing.data
y = california_housing.target 

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN 모델 초기화
knn = KNeighborsRegressor(n_neighbors=5, weights='uniform', algorithm='auto')

# 모델 학습
knn.fit(X_train, y_train)

# 예측
y_pred = knn.predict(X_test)

# 평가
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error :', mse)

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error

# 그리드 탐색을 위한 파라미터 그리드
param_grid = {
    'n_neighbors': [3,5,7],
    'weights': ['uniform', 'distance'],
    'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brrte']
}

# GridSearchCV를 사용하여 모델과 파라미터 그리드 설정
grid_search = GridSearchCV(knn, param_grid, scoring='neg_mean_squared_error', cv=5)

# 모델 학습 및 그리드 탐색 수행
grid_search.fit(X_train, y_train)

# 최적 모델 선택
best_model = grid_search.best_estimator_

# 최적 파라미터 확인
best_params = grid_search.best_params_
print('Best Parameters :', best_params)

# 예측
y_pred = best_model.predict(X_test)

# 평가
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error :', mse)