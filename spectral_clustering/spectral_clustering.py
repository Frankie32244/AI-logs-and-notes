# 1.计算相似度矩阵 -> 2.计算拉普拉斯矩阵 ->  3.使用谱聚类算法  
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.metrics import pairwise_distances

# 给定的10个二维数据点
data_points = np.array([
    [0.37454012, 0.95071431],
    [0.73199394, 0.59865848],
    [0.15601864, 0.15599452],
    [0.05808361, 0.86617615],
    [0.60111501, 0.70807258],
    [0.02058449, 0.96990985],
    [0.83244264, 0.21233911],
    [0.18182497, 0.18340451],
    [0.30424224, 0.52475643],
    [0.43194502, 0.29122914]
])

# 计算相似度矩阵（这里使用高斯核相似度）
def compute_similarity_matrix(X, sigma=1.0):
    dist_sq = pairwise_distances(X, squared=True)
    return np.exp(-dist_sq / (2 * sigma ** 2))

# 计算相似度矩阵
similarity_matrix = compute_similarity_matrix(data_points)
print("相似度矩阵：")
print(similarity_matrix)

# 计算拉普拉斯矩阵
degree_matrix = np.diag(np.sum(similarity_matrix, axis=1))
laplacian_matrix = degree_matrix - similarity_matrix
print("\n拉普拉斯矩阵：")
print(laplacian_matrix)

# 使用谱聚类算法
n_clusters = 3  # 设定要分成的簇数
spectral_model = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', random_state=42)
labels = spectral_model.fit_predict(similarity_matrix)

# 计算质心
centroids = np.array([data_points[labels == i].mean(axis=0) for i in range(n_clusters)])

# 可视化聚类结果
plt.figure(figsize=(8, 6))
for i in range(n_clusters):
    plt.scatter(data_points[labels == i][:, 0], data_points[labels == i][:, 1], label=f'Cluster {i}')
    # 绘制质心
    plt.scatter(centroids[i][0], centroids[i][1], s=200, marker='X', c='k', label=f'Centroid {i}')
    
plt.title('Spectral Clustering Result with Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()
