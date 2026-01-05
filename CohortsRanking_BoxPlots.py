import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ranking_matrix = pd.read_csv('PATH/to/ranks_df.csv',sep='\t',index_col=0)/50


df_transposed = ranking_matrix.T # Transpose the DataFrame to have the cohort subjects in the columns and the PRSs in the columns
column_medians = df_transposed.median() # Calculate the median of each member's ranking
sorted_columns = column_medians.sort_values().index # Sort the members based on their median values

# Plotting the ranking box plot
palette=sns.color_palette("coolwarm", len(df_transposed[sorted_columns].columns))
reversed_palette = palette[::-1]
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(data=df_transposed[sorted_columns], ax=ax, palette=reversed_palette)
ax.set_xlabel('Patient ID',fontsize=12)
ax.set_ylabel('Rank Quantile',fontsize=12)
ax.set_title("Rankings of 23 the individuals in OpenSNP given by 6 most consistent models",fontsize=14)
for i, col in enumerate(sorted_columns):
    median_val = column_medians[col]
    ax.text(i, median_val, f'{median_val:.2f}', ha='center', va='bottom', color=' black', fontsize=11, rotation=90, fontweight='bold')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()