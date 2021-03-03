import pandas as pd

df = pd.read_csv('D:\Chamber of Secrets\Python\CSV files\pokemon_data.csv')

# Read Headers
print(df.columns)

# Read Each Column
# Read first 5 names
print(df[['Name', 'Type 1', 'HP']][0:5])

# Read Each Row
print(df.iloc[0:4])

# Read a specfic location (R,C)
# Read Venusaur
print(df.iloc[2, 1])

# Read data through non-integer parameters
# Find pokemon which are primary fire types
print(df.loc[df['Type 1'] == 'Fire'])