import os
import pandas as pd

# Setting the directory containing each cohort idividuals folder
directory = 'PATH/to/directory/containing/each/individual/PLINK/files'

# RISK SCORES
individuals_scores = {}

for subdir, dirs,files in os.walk(directory):
# Iterate over each file for a specific individual
    for file in files:
    if file.endswith('.profile'):
    print(file)
    file_path = os.path.join(subdir, file)
    df = pd.read_table(file_path, delim_whitespace=True)
    print(df)
    # Extract the individual ID and PRS ID, the splits might require
    alteration according to the file names
    filename = os.path.splitext(file)[0]
    parts = filename.split('_')
    patient_name = parts[2]
    score_model = parts[4]
    # Extract the number of predictors loaded from the profile file
    score_value = df.iloc[-1, -1]
    # Add the score to the individuals_scores dictionary
    if patient_name not in individuals_scores:
        individuals_scores[patient_name] = {}
    individuals_scores[patient_name][score_model] = score_value

    
# Convert the individuals_scores dictionary to a DataFrame
scores_df = pd.DataFrame.from_dict(individuals_scores, orient='index')
scores_df.to_csv('PATH/to/scores_df.csv', sep='\t', index=True)


# RANKINGS
ranks_df=scores_df.rank(axis=0,ascending=False,method='min').astype(int)/50
ranks_df.to_csv('PATH/to/ranks_df.csv', sep='\t', index=True)


# VALID PREDICTORS
predictors_dict = {}

for subdir, dirs, files in os.walk(root_dir):
    # Iterate over each file for a specific individual
    for file in files:
        if file.endswith(".log"):
            # Extract the patient ID and PRS ID from the log file name, the splits might require alteration according to the file names
            patient_id = file.split('_')[0]+'_'+file.split("_")[1]
            print(patient_id)
            part_number = file.split("_")[3].split(".")[0]
            print(part_number)
            # Extract the number of predictors loaded from the log file
            predictors_loaded = None
            with open(os.path.join(subdir, file), "r") as log_file:
                for line in log_file:
                    if line.strip().endswith("valid predictors loaded."):
                        predictors_loaded = int(line.split()[1])
                        break
            # Add the score to the predictors_scores dictionary
            if patient_id not in predictors_dict:
                predictors_dict[patient_id] = {}
            predictors_dict[patient_id][part_number] = predictors_loaded

            
# Convert the dictionary to a DataFrame
valid_predictors_df = pd.DataFrame.from_dict(predictors_dict, orient="index")
valid_predictors_df.to_csv('PATH/to/valid_predictors_df.csv', sep='\t', index= True)