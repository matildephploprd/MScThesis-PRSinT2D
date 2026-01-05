import pandas as pd
from io import StringIO

 vcf_path = 'PATH/to/original/genotype.vcf'

# Read the VCF file
with open(vcf_path, 'r') as file:
    content = file.read()
# Separate header and data
data='\n'.join(line for line in content.split('\n') if not line.startswith('##'))
header = '\n'.join(line for line in content.split('\n') if line.startswith('##'))

# Load data into DataFrame
VCF_nodup = pd.read_csv(StringIO(data), sep='\t', low_memory=False)
column_name = VCF_nodup.columns[-1]
VCF_nodup = VCF_nodup.rename(columns={column_name: 'SampleName'})

# Remove variants with missing genotypes
VCF_nodup = VCF_nodup[~VCF_nodup['SampleName'].str.contains('\./\.')]

# Check for duplicates variants
duplicates = VCF_nodup[VCF_nodup.duplicated(subset=['ID'], keep=False)]
if duplicates.empty:
    print("No duplicates found in the ID column.")
else:
    print("There are duplicates found in the ID column")

# Group duplicates by 'ID' and check if all entries are identical
grouped = duplicates.groupby('ID')
results = []
for _, group_df in grouped:
    is_identical = group_df.iloc[:, 1:].apply(lambda x: x.nunique() == 1).all()
    results.append((group_df['ID'].iloc[0], is_identical))
    results_df = pd.DataFrame(results, columns=['ID', 'All_Columns_Identical'])
    only_true = results_df['All_Columns_Identical'].all()
print("All the duplicates are identical?:", only_true)

# Remove duplicate variants
VCF_nodup.drop_duplicates(subset=VCF_nodup.columns.difference(['ID']), inplace=True)
duplicates = VCF_nodup[VCF_nodup.duplicated(subset=['ID'], keep=False)]
if duplicates.empty:
    print("No duplicates found in the ID column.")
else:
    print("There are duplicates found in the ID column")

# Save the cleaned data to a new VCF file
combined_filename = "PATH/to/QCed/genotype.vcf"
with open(combined_filename, 'w') as file:
    file.write(header)
    file.write('\n')
    file.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSampleName\n")
    rows = '\n'.join('\t'.join(map(str, row.values)) for _, row in VCF_nodup.iterrows())
    file.write(rows)
print('Alterations saved')