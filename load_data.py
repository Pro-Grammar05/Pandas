import pandas as pd

# load data as csv file
df = pd.read_csv('D:\Chamber of Secrets\Python\CSV files\pokemon_data.csv')

# excel files - pd.read_excel
# text files - pd.read_csv('path', delimiter = '\t')

# print first and last 'n' rows of the data
print(df.head(3))
print(df.tail(3))