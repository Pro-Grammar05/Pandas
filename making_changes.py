import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# add column
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# remove column
df = df.drop(columns = ['Total'])

# faster way to add columns
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)
print(df.head(5))

# Rearrange columns
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))
