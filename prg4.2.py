import pandas as pd

df=pd.read_excel("Data_set.xls")
#print(df)

rajkot_students=df[df["City"]=="rajkot"]
print("student from rajkot city:")
print(rajkot_students)


male_students=df[df["Gender"]=="male"]
print("\n male students:")
print(male_students)


male_rajkot=df[(df["Gender"]=="male")&(df["City"]=="rajkot")]
print("\n male student from rajkot city:")
print(male_rajkot)


age_students=df[df["Age"]>=20]
print("\n students with age>=20:")
print(age_students)
