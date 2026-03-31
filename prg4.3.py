import pandas as pd

df=pd.read_excel("Data_set.xls")

df.loc[2,"Age"]=None
df.loc[5,"City"]=None

print("\n data after introducing missing values:")
print(df)

df_dropna=df.dropna()
print("\n result using dropna():")
print(df_dropna)
