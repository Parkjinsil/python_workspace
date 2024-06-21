from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 데이터 불러오기
wine = load_wine()
X = wine.data
y = wine.target 

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree 모델 생성
model = DecisionTreeClassifier(criterion='gini', max_depth=5, min_samples_split=2, min_samples_leaf=1)

# 모델 학습


model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.tree import plot_tree

# 탐색할 파라미터 그리드 설정
param_grid = {
    'criterion':['gini','entropy'],
    'max_depth':[3,5,7],
    'min_samples_split':[2,5,10],
    'min_samples_leaf':[1,3,5]
}

# GridSearchCV를 사용하여 최적 파라미터 탐색
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# 최적 파라미터 확인
best_params = grid_search.best_params_
print('Best Parameters :',best_params)

# 최적 모델로 예측
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:',accuracy)

# 트리 구조 시각화
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=wine.feature_names, class_names=wine.target_names, filled=True)
plt.show()

# 데이터 불러오기
wine = load_wine()
X = wine.data
y = wine.target

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Decision Tree 모델 생성
model = DecisionTreeClassifier(criterion='gini', max_depth=5, min_samples_split=2, min_samples_leaf=1)

# 모델 학습
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:',accuracy)

