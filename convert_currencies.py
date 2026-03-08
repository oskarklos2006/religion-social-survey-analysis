import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# Read the dataset
df = pd.read_csv('dataset.csv', low_memory=False)

ppp_conv = {
    'PL': 1.828,
    'US': 1,
    '': 0.7,
    'UK': 0.64,
}
# convert ppp to index against euro
ppp_conv_index = {k: v / ppp_conv[''] for k, v in ppp_conv.items()}

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def convert_income(value):
    if pd.isna(value):
        return np.nan
    if value == 'kann ich nicht sagen' or value == 'möchte ich nicht angeben':
        return np.nan
    number = re.findall('[0-9]+', value)
    return int(number[0])

# merge s18pl, s18us, s18uk into s18 calculating ppp conversion
def convert_and_merge(row):
    base_value = convert_income(row['S18'])
    if not represents_int(base_value):
        base_value = np.nan
    else:
        base_value = int(base_value)
    
    for country_code in ['PL', 'US', 'UK']:
        col_name = f'S18{country_code}'
        country_value = convert_income(row[col_name])
        if represents_int(country_value):
            country_value = int(country_value) / ppp_conv_index[country_code]
            if pd.isna(base_value) or country_value > base_value:
                base_value = country_value
                
    return round(base_value) if not pd.isna(base_value) else np.nan

df['S18'] = df.apply(convert_and_merge, axis=1)

bins = [-1, 749, 1249, 1749, 2499, 3499, 4999, 7499, 9999, float("inf")]

labels = [
    "<750",
    "750-1249",
    "1250-1749",
    "1750-2499",
    "2500-3499",
    "3500-4999",
    "5000-7499",
    "7500-9999",
    "10000+"
]

df["S18"] = pd.cut(
    df["S18"],
    bins=bins,
    labels=labels
)

print(df['S18'].value_counts(dropna=False))