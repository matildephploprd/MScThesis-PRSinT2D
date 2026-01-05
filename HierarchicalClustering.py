import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd

distance_matrix=pd.read_csv('PATH/to/distance_matrix.csv',sep='\t',index_col=0)
Z = linkage(distance_matrix.values, method='average')

# Plot dendrogram
plt.figure(figsize=(12, 6))
dendrogram(Z,labels=distance_matrix.index, color_threshold=221, leaf_rotation=90)
plt.title("PRS hierarchical clustering based on ranking", fontsize=16)
plt.xlabel('PRS ID', fontsize=14)
plt.ylabel('Distance', fontsize=14)
plt.tick_params(axis='y', which='major', labelsize=12)
plt.tick_params(axis='x', which='major', labelsize=12)
plt.show()