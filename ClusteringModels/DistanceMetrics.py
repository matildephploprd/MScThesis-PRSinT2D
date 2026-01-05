import pandas as pd
import numpy as np

ranking_df=pd.read_csv('PATH/to/rank_matrix.csv',sep='\t',index_col=0)

# KENDALL'S TAU DISTANCE
def kendalls_tau_distance(tau1, tau2):
    n = len(tau1)
    if np.array_equal(tau1, tau2):
        return 0
    max_discordant_pairs = n * (n - 1) / 2
    discordant_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (tau1[i] < tau1[j] and tau2[i] > tau2[j]) or (tau1[i] > tau1[j] and tau2[i] < tau2[j]):
                discordant_pairs += 1
    kendalls_tau = discordant_pairs
    return kendalls_tau


#Calculating the kendall's tau distance matrix
distance_matrix = pd.DataFrame(0, index=ranking_df.columns, columns=ranking_df.columns)
for i, col1 in enumerate(ranking_df.columns):
    for j, col2 in enumerate(ranking_df.columns):
        if i < j:
            tau_distance = kendalls_tau_distance(ranking_df[col1], ranking_df[col2])
            distance_matrix.at[col1, col2] = tau_distance
            distance_matrix.at[col2, col1] = tau_distance

            
# SPEARMAN FOOTRULE DISTANCE
def spearmans_footrule_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The lists must have the same length.")
        differences = [abs(rank1 - rank2) for rank1, rank2 in zip(list1, list2)]
        distance = sum(differences)
        return distance

# Calculating the Spearman's tau distance matrix
spearman_distance= pd.DataFrame(index=ranking_df.columns, columns=ranking_df.columns)
for col1 in ranking_df.columns:
    for col2 in ranking_df.columns:
        distance=spearmans_footrule_distance(ranking_df[col1], ranking_df[col2])
        spearman_distance.at[col1, col2] = distance
        spearman_distance.at[col2, col1] = distance
        spearman_distance = spearman_distance.astype(float)

distance_matrix.to_csv('PATH/to/distance_matrix.csv', sep='\t', index=True)
spearman_distance.to_csv('PATH/to/spearman_distance.csv', sep='\t', index=True)
