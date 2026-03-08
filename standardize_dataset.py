import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('dataset.csv', low_memory=False)

print(df['S8'].value_counts(dropna=False))

# Fill missing in F3.2 with 0, convert to buckets
df['F3_2'] = pd.to_numeric(df['F3_2'], errors='coerce').fillna(0)
bins = [0, 500, 1000, 2000, 5000, 10000, 15000, 25000, 50000, 100000]
bins_labels = ['0-499', '500-999', '1000-1999', '2000-4999', '5000-9999', '10000-14999', '15000-24999', '25000-49999', '50000-99999']
df['F3_2'] = pd.cut(df['F3_2'], bins=bins, labels=bins_labels, right=False)
print(df['F3_2'].value_counts().sort_index())

# Zero-out child amounts over 15 in S6_1
df['S6_1'] = pd.to_numeric(df['S6_1'], errors='coerce').fillna(0)
df.loc[df['S6_1'] > 15, 'S6_1'] = 0

# Replace non-answered values in school leaving age column with 0
df['S8'] = pd.to_numeric(df['S8'], errors='coerce').fillna(0)

# merge s905 and s905or into one column, preferring s905 values
df['S905'] = df['S905'].combine_first(df['S905or'])

# Drop unnecessary columns
# S17_1-S17_4 -> related to mobile/landline connections, only DE
# S20_(1-10) -> related to statements familiar to person, only UK
# S906 -> british citizenship, only DE
# S9_6(1-2) -> where parents were born, only DE
# S15(DE/FR/UK/NL/ES/PL/USA) -> favored political party, country-specific
# F18.1.(8,8o) -> open question for discrimination
# F17.2.12o -> open question for voluntary involvement  
# F3.4(5o,6o) -> what donated to charity
columns_to_drop = ['S17_1', 'S17_2', 'S17_3_1','S17_3_2','S17_3_3', 'S17_5', 
                     'S20_1', 'S20_2', 'S20_3', 'S20_4', 'S20_5',
                        'S20_6', 'S20_7', 'S20_8', 'S20_9', 'S20_10', 'S905or', 'S906',
                        'S9_6_1','S9_6_1or', 'S9_6_2', 'S9_6_2or',
                        'S15DE', 'S15FR', 'S15UK', 'S15NL', 'S15ES', 'S15PL', 'S15US',
                        'F18_1_8', 'F18_1_8o', 'F17_2_12o', 'F3_4_5o', 'F3_4_6o'
                        ]
df = df.drop(columns=columns_to_drop)

# print(df['S905or'].value_counts(dropna=False))