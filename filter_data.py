import pandas as pd
import re

df = pd.read_csv('D:\Chamber of Secrets\Python\CSV files\pokemon_data.csv')

# Use conditional operatores for more than one condition
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# reset indexes
new_df = new_df.reset_index(drop = True)

# text-based filtering
new_df = df.loc[~df['Name'].str.contains('Mega')]

# regex filtering
new_df = df.loc[df['Name'].str.contains('^pi[a-z]', flags = re.I, regex = True)]
print(new_df)