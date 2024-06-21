import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 클러스터 데이터 생성
X, y = make_blobs(n_samples=500, centers=4, cluster_std=0.6, random_state=0)

# K-평균 군집화 모델 생성 및 학습
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

# 군집 레이블 출력
print('Labels:', kmeans.labels_)

# 군집 중심점 출력
print('Cluster centers:', kmeans.cluster_centers_)

# 시각화
plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='r',
marker='x')
plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 연령과 연간 소득 데이터를 사용하여 고객을 세그먼트화
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 고객 데이터 생성(연령, 소득)
X = np.array([[35,50000],[45,85000],[25,35000],
              [30,60000],[55,100000],[40,70000],
              [60,90000],[50,80000],[35,55000]])

# K-평균 군집화 모델 생성 및 학습 (k=3)
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# 군집 레이블 출력
print('Labels:',kmeans.labels_)

# 군집 중심점 출력
print('Cluster centers: ',kmeans.cluster_centers_)

# 시각화
plt.scatter(X[:,0],X[:,1],c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='r', marker='*', label='Centroids')
plt.title("K-Means Customer Segmentation")
plt.xlabel("Age")
plt.ylabel("Annual Income ($)")
plt.legend()
plt.show()