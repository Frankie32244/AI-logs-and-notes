import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances

class SpectralClustering:
    def __init__(self, n_clusters=2, sigma=1.0, random_state=None):
        """
        初始化谱聚类类的参数。
        
        :param n_clusters: 聚类的数量
        :param sigma: 高斯核函数的标准差参数，用于控制相似度矩阵
        :param random_state: 随机种子，用于确保 K-Means 聚类的可重复性
        """
        self.n_clusters = n_clusters
        self.sigma = sigma
        self.random_state = random_state

    def _compute_similarity_matrix(self, X):
        """
        计算相似度矩阵。
        
        :param X: 数据点的二维数组，形状为 (n_samples, n_features)
        :return: 相似度矩阵 (n_samples, n_samples)
        """
        dist_sq = pairwise_distances(X, squared=True)
        similarity_matrix = np.exp(-dist_sq / (2 * self.sigma ** 2))
        return similarity_matrix

    def _compute_laplacian_matrix(self, similarity_matrix):
        """
        计算未归一化的拉普拉斯矩阵。
        
        :param similarity_matrix: 相似度矩阵 (n_samples, n_samples)
        :return: 拉普拉斯矩阵 (n_samples, n_samples)
        """
        degree_matrix = np.diag(np.sum(similarity_matrix, axis=1))
        laplacian_matrix = degree_matrix - similarity_matrix
        return laplacian_matrix

    def fit_predict(self, X):
        """
        对数据进行谱聚类并返回每个样本的聚类标签。
        
        :param X: 输入数据点 (n_samples, n_features)
        :return: 每个样本的聚类标签 (n_samples,)
        """
        # Step 1: 计算相似度矩阵
        similarity_matrix = self._compute_similarity_matrix(X)

        # Step 2: 计算拉普拉斯矩阵
        laplacian_matrix = self._compute_laplacian_matrix(similarity_matrix)

        # Step 3: 计算拉普拉斯矩阵的特征值和特征向量
        eigvals, eigvecs = np.linalg.eigh(laplacian_matrix)

        # Step 4: 选择前 n_clusters 个特征向量
        X_transformed = eigvecs[:, :self.n_clusters]

        # Step 5: 对嵌入后的特征向量进行 K-Means 聚类
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        labels = kmeans.fit_predict(X_transformed)

        return labels



import matplotlib.pyplot as plt

# 示例数据点
data_points = np.array([
    [0.1, 0.6], [0.15, 0.71], [0.08, 0.9], [0.16, 0.85],
    [0.85, 0.15], [0.9, 0.2], [0.76, 0.3], [0.8, 0.25]
])

# 创建并执行谱聚类
spectral_clustering = SpectralClustering(n_clusters=2, sigma=0.1, random_state=42)
labels = spectral_clustering.fit_predict(data_points)

# 可视化聚类结果
plt.scatter(data_points[:, 0], data_points[:, 1], c=labels, cmap='viridis')
plt.title('Spectral Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()

