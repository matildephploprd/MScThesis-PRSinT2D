og_score_path = 'PATH/to/original/PRS/file'
score = pd.read_csv(og_score_path)
new_score = score.copy()
new_score=new_score[['SNP_code', 'effect_allele','effect_weight']]
new_new_score.rename(columns={'SNP_code':'ID'},inplace=True)
score.to_csv('PATH/to/PRS/PLINK/format.txt', sep=' ', index=False)
