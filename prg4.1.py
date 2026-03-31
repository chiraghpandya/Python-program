import pandas as pd

df=pd.read_excel("Data_set.xls")
print(df)

print("column names")
print(df.columns)

print("Data type of column")
print(df.dtypes)

print("Top 5 record display")
print(df.head())

print("Last 5 record display")
print(df.tail())
