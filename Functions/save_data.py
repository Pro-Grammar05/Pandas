import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# Save as csv
# Save without excel
# Save without index
df.to_csv('modified.csv', index = False)
df.to_excel('modified.xlsx', index = False)
