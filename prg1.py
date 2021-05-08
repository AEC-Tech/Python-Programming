import pandas as pd

s1 = pd.Series(data=[90,93,98,96,94], index=['Ankit','Rahul','Payal','Ajay','Bhumika'],dtype=float)

print(s1.sort_values(ascending=False))
s1.name = "testing"
print(s1.name)
dg = pd.read_csv("student.csv")
print(dg)