import pandas as pd

#Load 
df = pd.read_csv('titanic.csv')

#Prints first 5 rows
print(df.head())

# Some simple Pandas operations
print(df.describe()) #shows summary of stats(numerical columns)
print(df['Survived'].value_counts()) #gets specifc column; value count shoes how many times each unique value appears in a column.
