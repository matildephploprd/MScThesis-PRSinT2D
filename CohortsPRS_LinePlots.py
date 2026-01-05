import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sort the keys of plotted_dict alphabetically
scores_df=pd.read_csv('PATH/to/scores_df.csv',sep='\t',index_col=0)
plotted_dict = scores_df.to_dict(orient='list')
sorted_keys = sorted(plotted_dict.keys())

# Plotting the risks
fig = plt.figure(figsize=(15, 6))
palette = sns.color_palette("viridis", n_colors=len(sorted_keys))
for i, key in enumerate(sorted_keys):
    value = plotted_dict[key]
    plt.plot(range(1, len(value) + 1), value, label=key, color=palette[i % len(palette)])
    plt.text(len(value), value[-1], key, fontsize=10, color=palette[i % len(palette)], ha='center', va='center')
    plt.xlabel('Patient ID',fontsize=12)
    plt.ylabel('Risk',fontsize=12)
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.2), fontsize=11)
    plt.yticks(fontsize=12)
    plt.xticks(range(1, len(scores_df) + 1), scores_df.index, rotation=60, fontsize=12, ha='right') 
    plt.show()