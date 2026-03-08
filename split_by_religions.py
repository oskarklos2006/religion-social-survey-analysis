import csv
import pandas as pd
import pandasql as pdsql


df=pd.read_csv('dataset.csv',low_memory=False)

df['country'] = df['country'].astype("string")
print(df['country'].dtypes)
df_islam = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'Islam'")
islam_csv_file = 'islam.csv'
df_islam.to_csv(islam_csv_file, index=False)

df_christ = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'Christentum'")
christ_csv_file = 'christianity.csv'
df_christ.to_csv(christ_csv_file, index=False)

df_jude = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'Judentum'")
jude_csv_file = 'jews.csv'
df_jude.to_csv(jude_csv_file, index=False)

df_hindu = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'Hinduismus'")
hindu_csv_file = 'hinduism.csv'
df_hindu.to_csv(hindu_csv_file, index=False)

df_buddhism = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'Buddhismus'")
buddhism_csv_file = 'buddhism.csv'
df_buddhism.to_csv(buddhism_csv_file, index=False)

df_other = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'andere Religionsgemeinschaft'")
other_csv_file = 'other_religions.csv'
df_other.to_csv(other_csv_file, index=False)

df_atheists = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'keine Religionsgemeinschaft'")
atheists_csv_file = 'atheists.csv'
df_atheists.to_csv(atheists_csv_file, index=False)

df_unknown = pdsql.sqldf("SELECT * FROM df WHERE F7 = 'kann ich nicht sagen OR möchte ich nicht angeben'")
unknown_csv_file = 'unknown.csv'
df_unknown.to_csv(unknown_csv_file, index=False)