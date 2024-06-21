from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# 캘리포니아 집값 데이터셋 로드
california_housing = fetch_california_housing(as_frame=True)
x = california_housing.data
y = california_housing.target 

# 데이터셋을 학습용과 테스트용으로 분할
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Decision Tree Regression 모델 생성 및 학습
model3 = DecisionTreeRegressor(max_depth=5, min_samples_split=2, min_samples_leaf=1)
model3.fit(x_train, y_train)

# 학습된 모델로 테스트 데이터 예측
y_pred = model3.predict(x_test)

# 예측 결과 평가
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:',mse)

from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.tree import plot_tree

# 탐색할 파라미터 그리드 설정
param_grid = {
    'max_depth':[3,5,7],
    'min_samples_split':[2,5,7],
    'min_samples_leaf':[1,3,5]
}

# GridSearchCV를 사용하여 최적 파라미터 탐색
grid_search = GridSearchCV(model3, param_grid, cv=5)
grid_search.fit(x_train, y_train)

best_params = grid_search.best_params_
print('Best Parameters:',best_params)

# 최적 모델로 예측
best_model = grid_search.best_estimator_
y_pred = best_model.predict(x_test)

# 평가
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:',mse)



