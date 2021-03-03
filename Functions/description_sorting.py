import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# get statistical info
print(df.describe())

# sort values by different parameters
# 'False' makes it reverse
print(df.sort_values(['Name']))
print(df.sort_values(['Type 1', 'HP'], ascending = False))
