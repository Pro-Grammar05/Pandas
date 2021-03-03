import pandas as pd

df = pd.read_csv('D:\Chamber of Secrets\Python\CSV files\pokemon_data.csv')

# Mean value of stats sorted by type
# Sort the values by a parameter in ascending or descending order
print(df.groupby(['Type 1']).mean().sort_values('HP', ascending = False))

# count number of pokemon of each type
df['count'] = 1
print(df.groupby(['Type 1']).count()['count'])