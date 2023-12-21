import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 设置随机种子
np.random.seed(42)

# 生成数据
# 深度在 -100 到 -75 米，速率大约以 -0.6m/s 为中心
depth1 = -75 - 25 * np.random.rand(100, 1)
rate1 = -0.6 + 0.1 * np.random.randn(100, 1)

# 深度在 -75 到 -30 米，速率大约以 -0.8m/s 为中心
depth2 = -30 - 45 * np.random.rand(100, 1)
rate2 = -0.8 + 0.1 * np.random.randn(100, 1)

# 深度在 -30 到 0 米，速率大约以 -1.1m/s 为中心
depth3 = -30 * np.random.rand(100, 1)
rate3 = -1.1 + 0.1 * np.random.randn(100, 1)

# 合并数据
data = np.vstack((np.hstack((depth1, rate1)), np.hstack((depth2, rate2)), np.hstack((depth3, rate3))))

# 使用K均值聚类算法
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(data)

# 可视化聚类结果
plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis', s=50, alpha=0.8)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.xlabel('Depth (meters)')
plt.ylabel('Rate (m/s)')
plt.title('Diving Rate Clustering at Different Depths')
plt.legend()
plt.show()
