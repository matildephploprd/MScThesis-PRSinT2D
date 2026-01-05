import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Loading the necessary data for the cohort
risks_df = pd.read_csv('PATH/to/risk_matrix.csv',sep='\t',index_col=0)
ranks_df = pd.read_csv('PATH/to/rank_matrix.csv',sep='\t',index_col=0)
valid_pred_df= pd.read_csv('PATH/to/valid_pred_matrix.csv',sep='\t',index_col=0)

# (Example for Bin 1)
selected_scores = ['PGS000031','PGS000805','PGS000868', 'PGS003729','PGS003733']

# Decide a default ranking order
ordered_rank = ranks_df.sort_values(by='PGS000031')

# Plotting
color_map = plt.cm.get_cmap('RdBu', len(ordered_rank))
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

plotted_rows = set()
for idx, (index, row) in enumerate(ordered_rank.iterrows()):
    color = color_map(idx)
    for col in selected_scores:
        if col in scores_df.columns and col in valid_pred_df.columns:
            x = scores_df.loc[index, col]
            y = row[col]
            z = valid_pred_df.loc[index, col]
            ax.scatter(x, y, z, alpha=1, color=color)
            # Annotating the PGS ID
            if idx == 0: # Only add text label for the first element plotted
                ax.text(x, y, z, col, fontsize=8, color='black', ha='right', va='bottom')
ax.set_xlabel('risk')
ax.set_ylabel('rank')
ax.set_zlabel('valid predictors')
ax.view_init(elev=20, azim=20) # Change the angles to get different views
ax.set_ylim(0, 1)
plt.title('Risk vs Rank vs Valid Predictors - Bin 1')
custom_lines = [plt.Line2D([0], [0], marker='o', color=color_map(i), linestyle='None', markersize=10) for i in range(len(ordered_rank))]
row_labels = ordered_rank.index.tolist()
# Anottating the individuals label
ax.legend(custom_lines, row_labels, ncol=2, loc='upper left', bbox_to_anchor=(1,1))
plt.show()
