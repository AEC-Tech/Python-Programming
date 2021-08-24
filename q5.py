import pandas as pd
data = {"Name" :["Toshi","Bhawana","Samridhi"],
        "Age":[16,17,18],
        "Weight":[45,50,48]}
df = pd.DataFrame(data,index=['Row_1',"Row_2","Row_3"])
print(df)
#df.loc['Row_2','Age':'Weight'] = [18,52]
df.iloc[1,1:3] = [18,52]
print("Updated data frame is ")
print(df)