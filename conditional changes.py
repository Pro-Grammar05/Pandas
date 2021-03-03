import pandas as pd

df = pd.read_csv('D:\Chamber of Secrets\Python\CSV files\pokemon_data.csv')

# change fire types to flamer types
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df)