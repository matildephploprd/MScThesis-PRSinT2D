import os
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Creating a dictionary containing all the PRSs
def dict_all_models(list_files,directory):
    dataframes_dict = {}
    for file in list_files:
        if file.endswith('.csv'):
            complete_file=os.path.join(directory,file)
            key = file.split('_')[2]
            df = pd.read_csv(complete_file,sep=',',header=0) 
            dataframes_dict[key] = df
            print(key)
    return dataframes_dict


# Creating a dictionary with all of the variants per PRS
def file_SNP_code(dataframes_dict):
    files_variants = {}
    for file, df in dataframes_dict.items():
        print(file)
        hm_rsID_column = list(set(df['SNP_code'].tolist()))
        files_variants[file] = hm_rsID_column
    return files_variants


# Creating a dictionary with each SNP number of occurrences. Sets the SNPs as the keys and the number of appearances as the values
def counting_variants(files_variants):
    counting_var={}
    for model, value_list in files_variants.items():
        print(model)
        for value in value_list:
            if value in counting_var:
                counting_var[value] += 1
            else:
                counting_var[value] = 1
    return counting_var


# Create a dictionary that has as keys the number of appearances (can range from 1-64) and as values, the number of SNPs that appear said times
def appearances(variants_counts):
    all_values = list(variants_counts.values())
    value_counts = Counter(all_values)
    value_counts_sorted = {k: value_counts[k] for k in sorted(value_counts)}
    return value_counts_sorted



harmonized_files_directory = 'PATH/to/harmonized/PGS/files'
harmonized_files = os.listdir(harmonized_files_directory)
harmonized_files.sort()
print('working scoring files:',len(harmonized_files))
all_scores_dict= dict_all_models(harmonized_files,harmonized_files_directory)
SNP_per_file =file_SNP_code(all_scores_dict)
SNP_counts = counting_variants(SNP_per_file)
print('Number of SNPs', len(SNP_counts))
appearances = appearances(SNP_counts)


# Plotting the distribution
values, frequencies = zip(*appearances.items())
plt.figure(figsize=(12, 4.5)) # Adjust the figure size
plt.bar(values, frequencies, edgecolor='k', alpha=0.7, color='skyblue')
tick_positionsx = np.arange(1, 65, step=1)
plt.xticks(tick_positionsx,rotation=45)
plt.xlim(0, 65)
plt.xlabel('Number of files containing a certain SNP')
plt.ylabel('Frequency of SNPs')
plt.title('Distribution of SNP occurences across the 64 PRSs')
plt.show()