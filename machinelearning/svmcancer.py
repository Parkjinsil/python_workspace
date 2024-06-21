from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# 유방암 데이터셋 로드
cancer = load_breast_cancer()
x = cancer.data
y = cancer.target 

# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 커널 종류 리스트
kernel_list = ['linear', 'poly', 'rbf']

# 각 커널 종류에 대해 모델 학습 및 평가
for kernel in kernel_list:
    # SVM 모델 초기화
    svm = SVC(kernel=kernel)
    
    # 모델 학습
    svm.fit(x_train, y_train)
    
    # 예측
    y_pred = svm.predict(x_test)
    
    # 분류 보고서 출력
    print(f'Kernel:{kernel}')
    print(classification_report(y_test,y_pred))
    print('='*50)
    
import pandas as pd
    
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df['target'] = pd.Series(cancer.target)
    
# 데이터셋 정보 출력
    
df.head() # 표준화되기 전의 데이터 출력
    
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
    
# 데이터 표준화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# SVM 모델 초기화
svm = SVC(kernel='rbf')

# 모델 학습
svm.fit(x_train, y_train)

# 예측
y_pred = svm.predict(x_test)

# 정확도 평가
print(classification_report(y_test, y_pred))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# 2차원 데이터
x = [1,2,3,4,5]
y = [2,4,6,8,10]
labels = [0,1,0,1,0]

# 3차원 변환
z = np.square(x) + np.square(y)

# 3D 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 데이터 포인트 플롯
ax.scatter(x,y,z,c=labels)

# 축 라벨 성정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 그래프 출력
# plt.show()

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# 유방암 데이터셋 로드
cancer = load_breast_cancer()

# 데이터셋을 pandas DataFrame으로 변환
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(cancer.data)

# 스케일링된 데이터를 DataFrame으로 변환
df_scaled = pd.DataFrame(X_scaled, columns=cancer.feature_names)
df_scaled['target'] = pd.Series(cancer.target)

df_scaled.head()

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# TSNE 적용
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

# 시각화
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=cancer.target)
plt.xlabel("t_SNE dimension 1")
plt.ylabel("t_SNE dimension 2")
plt.title("t_SNE visualization of Breast cancer")
plt.colorbar()
plt.show()




