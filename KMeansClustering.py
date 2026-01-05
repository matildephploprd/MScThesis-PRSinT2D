from sklearn.cluster import KMeans
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

distance_matrix=pd.read_csv('PATH/to/distance_matrix.csv',sep='\t',index_col=0)

# Determining nr clusters - Elbow method
wcss=[]
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, n_init=10, random_state=42)
    kmeans.fit(distance_matrix)
    wcss_iter = kmeans.inertia_
    wcss.append(wcss_iter)

number_clusters = range(1,11)
plt.plot(number_clusters,wcss)
plt.grid(axis='y')
plt.title('Elbow method kendall tau distance - OpenSNP')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

# K-Means clustering
kmeans = KMeans(n_clusters=4, n_init=10, random_state=42)
kmeans.fit(distance_matrix)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
cluster_labels_df = pd.DataFrame({'Cluster_Labels': labels}, index=
distance_matrix.index)
cluster_labels_df = cluster_labels_df.sort_values(by='Cluster_Labels')

# PCA dimensionality reduction
pca = PCA(n_components=3)
principal_components = pca.fit_transform(distance_matrix)
principal_distance_matrix = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3'], index=distance_matrix.index)
merged_data = pd.merge(principal_distance_matrix, cluster_labels_df, left_index=True, right_index=True)
print(merged_data.sort_index())

# pPotting the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
cluster_labels_plot = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4']
colors = ['darkorange', 'orangered', 'deeppink', 'darkviolet']
text_labels = merged_data.index.astype(str)

for i, color in enumerate(colors):
    # Select data for each cluster
    ix = merged_data['Cluster_Labels'] == i
    ax.scatter(np.array(merged_data['PC1'])[ix],
               np.array(merged_data['PC2'])[ix],
               np.array(merged_data['PC3'])[ix],
               c=color,
               label=cluster_labels_plot[i],
               s=50,
               alpha=1)
    
for i, txt in enumerate(text_labels):
    ax.text(merged_data['PC1'][i], merged_data['PC2'][i], merged_data['PC3'][i],txt, color='black', fontsize=8)
ax.set_xlabel('PC1 \n (x% of data variance)', fontsize=12)
ax.set_ylabel('PC2 \n (y% of data variance)', fontsize=12)
ax.set_zlabel('PC3 \n (z% of data variance)', fontsize=12)
ax.set_title("PRS K-Means clustering based on ranking", fontsize=14)
ax.legend(loc='upper right',bbox_to_anchor=(1.23, 1.11), fontsize=10)
plt.tick_params(axis='y', which='major', labelsize=12) # Increase size of y-axis labels
plt.tick_params(axis='x', which='major', labelsize=12)
plt.tick_params(axis='z', which='major', labelsize=12)
plt.show()