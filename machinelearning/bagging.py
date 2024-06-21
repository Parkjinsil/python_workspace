from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_diabetes
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate

from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


from sklearn.ensemble import BaggingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor

iris = load_iris()
wine = load_wine()
cancer = load_breast_cancer()

'''
파이프라인이란?
: 머신러닝에서 여러 단계를 순서대로 묶어 한 번에 처리할 수 있게 해주는 도구
  데이터 전처리, 변환, 모델 학습/예측 단계를 하나의 객체로 관리 가능
  -> 데이터 처리 과정이 간단해지고 , 실수 줄일 수 있음
'''

# ex) 데이터를 정리하고 정리된 데이터로 예측 모델을 만들고 싶다면 이런 파이프 라인 생성
KB_model = make_pipeline(
    StandardScaler(),       # 데이터 정리 : 데이터를 표준화(평균 0, 분산 1)
    KNeighborsClassifier()  # 모델 만들기 : K-최근접 이웃(K-Nearest Neighbors, KNN)모델 사용
)

# 배깅 모델 : 여러개의 기본 모델을 사용하여 더 강력한 모델을 만드는 방법
# ex) 여러 개의 KNN모델을 만들어서 각각의 결과를 결합
bagging_model = BaggingClassifier(KB_model, n_estimators=100, max_samples=0.9, max_features=0.9)
#               10개의 기본 학습기 사용, 각 기본 학습기는전체 데이터 샘플의 50% ,전체 특성의 50% 사용   
cross_val = cross_validate(
    estimator = KB_model,             # 평가할 모델
    X = iris.data, y = iris.target,   # x : 특성 데이터 / y : 타겟 데이터
    cv=5                              # 5-폴드 교차 검증 수행
)

print('KNN-iris')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))     # 각 폴드에 대한 모델 학습 시간
print('Average Score Time : {}'.format(cross_val['score_time'].mean())) # 각 폴드에 대한 모델 평가 시간
print('Average Test Score : {}'.format(cross_val['test_score'].mean())) # 각 폴드에 대한 모델의 테스트 점수

cross_val = cross_validate(
    estimator = bagging_model,
    X = iris.data, y = iris.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = KB_model,
    X = wine.data, y = wine.target,
    cv=5
)

print('KNN-wine')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = bagging_model,
    X = wine.data, y = wine.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = KB_model,
    X = cancer.data, y = cancer.target,
    cv=5
)

print('KNN-cancer')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = bagging_model,
    X = cancer.data, y = cancer.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

'''
SVM : 분류 문제에서 두 클래스 간의 경계(결정 경계)를 찾는 알고리즘
SVC() : SVM을 사용하여 데이터를 분류
'''

SB_model = make_pipeline(
    StandardScaler(),  # 데이터 전처리 단계 : 데이터 표준화
    SVC()              # 모델 학습 단계 : Support Vector Machine(SVM) 분류기 모델 
)

Sbagging_model = BaggingClassifier(SB_model, n_estimators=10, max_samples=0.5, max_features=0.5)

cross_val = cross_validate(
    estimator = SB_model,
    X = iris.data, y = iris.target,
    cv=5
)

print('SVC-iris')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = Sbagging_model,
    X = iris.data, y = iris.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = SB_model,
    X = wine.data, y = wine.target,
    cv=5
)

print('SVC-wine')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = Sbagging_model,
    X = wine.data, y = wine.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = SB_model,
    X = cancer.data, y = cancer.target,
    cv=5
)

print('SVC-cancer')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = Sbagging_model,
    X = cancer.data, y = cancer.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

'''
Decision Tree : 데이터 특징을 이용해 예측하기 위한 분류 및 회귀 모델
- 작동방식 
  : 데이터를 여러 질문(조건)에 따라 분할하여 트리 구조 만듦
  -> 각 노드는 질문에 대한 답(조건)에 따라 데이터를 나눔
  -> 리프 노드(최종 노드)에는 예측 결과가 들어감
DecisionTreeClassifier() : Decision Tree 알고리즘을 사용하여 데이터를 분류
'''

DB_model = make_pipeline(
    StandardScaler(),
    DecisionTreeClassifier()
)

Dbagging_model = BaggingClassifier(DB_model, n_estimators=10, max_samples=0.5, max_features=0.5)

cross_val = cross_validate(
    estimator = DB_model,
    X = iris.data, y = iris.target,
    cv=5
)

print('Decision Tree - iris')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = Dbagging_model,
    X = iris.data, y = iris.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = DB_model,
    X = wine.data, y = wine.target,
    cv=5
)

print('Decision Tree - wine')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = Dbagging_model,
    X = wine.data, y = wine.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = DB_model,
    X = cancer.data, y = cancer.target,
    cv=5
)

print('Decision Tree - cancer')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = Dbagging_model,
    X = cancer.data, y = cancer.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))





print('---------------------------------------------------')




california = fetch_california_housing()
diabetes = load_diabetes()

RB_model = make_pipeline(
    StandardScaler(),
    KNeighborsRegressor()
)

# Bagging Regressor
Rbagging_model = BaggingRegressor(RB_model, n_estimators=10, max_samples=0.3, max_features=0.5)

cross_val = cross_validate(
    estimator=RB_model,
    X = california.data, y = california.target,
    cv=5
)

print('knn-california')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator=Rbagging_model, # Bagging model with KNN regression
    X = california.data, y = california.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator=RB_model,
    X = diabetes.data, y = diabetes.target,
    cv=5
)

print('knn-diabetes')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator=Rbagging_model, # Bagging model with KNN regression
    X = diabetes.data, y = diabetes.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

SVRB_model = make_pipeline(
    StandardScaler(),
    SVR()
)

# BaggingRegressor 샘플사이즈 축소(0.3)
SVRbagging_model = BaggingRegressor(SVRB_model, n_estimators=10, max_samples=0.3, max_features=0.5)

cross_val = cross_validate(
    estimator=SVRB_model, # SVM Regression model
    X = california.data, y = california.target,
    cv=5
)

print('SVR-california')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator=SVRbagging_model, # Bagging with SVM Regression model
    X = california.data, y = california.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator=SVRB_model, # SVM Regression model
    X = diabetes.data, y = diabetes.target,
    cv=5
)

print('SVR-diabetes')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator=SVRbagging_model, # Bagging with SVM Regression model
    X = diabetes.data, y = diabetes.target,
    cv=5
)

print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor

RF_model = make_pipeline(
    StandardScaler(),
    RandomForestClassifier()
)

cross_val = cross_validate(
    estimator = RF_model, # SVM Regression model
    X = iris.data, y = iris.target,
    cv=5
)

print('Random Forest-iris')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = RF_model, # SVM Regression model
    X = wine.data, y = wine.target,
    cv=5
)

print('Random Forest-wine')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))

cross_val = cross_validate(
    estimator = RF_model, # SVM Regression model
    X = cancer.data, y = cancer.target,
    cv=5
)

print('Random Forest-cancer')
print('Average Fit Time : {}'.format(cross_val['fit_time'].mean()))
print('Average Score Time : {}'.format(cross_val['score_time'].mean()))
print('Average Test Score : {}'.format(cross_val['test_score'].mean()))
