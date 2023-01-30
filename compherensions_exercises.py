# Bir Veri Setindeki Değişkenlerin İsimlerinin Değiştirilmesi

'''import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns

A = []

for col in df.columns:
    A.append(col.upper())


df_columns = [col.upper() for col in df.columns]'''

# İsminde 'INS' olan ifadelere FLAG ekle diğerlerine ise NO_FLAG

'''import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns

df.columns = [col.upper() for col in df.columns]

['FLAG_' + col if 'INS' in col else 'NO_FLAG_' + col for col in df.columns]
'''
# Amaç key'i string value'su string listesi olan bir sözlük
# sadece sayısal değişkenler için yapmak istiyoruz

'''import seaborn as sns

df = sns.load_dataset('car_crashes')
df.columns

num_cols = [col for col in df.columns if df[col].dtype != 'O']
dict1 = {}
agg_list = ['mean', 'min', 'max', 'sum']

for col in num_cols:
    dict1[col] = agg_list
#kısa yol
new_dict1 = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict1)'''
import pandas as pd
import seaborn as sns

df = sns.load_dataset('car_crashes')
df.columns

num_cols1 = [col for col in df.columns if df[col].dtype != 'O']

soz = {}
agg_list = ['mean', 'min', 'max', 'sum']

for col in num_cols1:
    soz[col] = agg_list

#kısa yol
new_dict = {col: agg_list for col in num_cols1}

df[num_cols1].head()

df1 = df[num_cols1].agg(new_dict)

with pd.ExcelWriter('data.xlsx') as writer:
    df1.to_excel(writer, sheet_name='pydeneme')