import pandas as pd
data = {"Age":[16,18,17],"Name":['Shreya','Bhawana','Pooja']}
df = pd.DataFrame(data)
print(df)
for k in df.iterrows():
    print(k[1]["Name"], " is ",k[1]["Age"]," year old")