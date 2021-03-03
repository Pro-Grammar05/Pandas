import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# change fire types to flamer types
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df)
