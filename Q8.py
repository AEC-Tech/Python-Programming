import pandas as pd
data = {"Name" :["Toshi","Bhawana","Samridhi"],
        "Age":[16,17,18],
        "Weight":[45,50,48]}
df = pd.DataFrame(data,index=['Row_1',"Row_2","Row_3"])
print(df)
print("Column Labels are ",df.columns)
print("Row labels are ",df.index)
print("Data types are ",df.dtypes)
print("Dimension is ",df.ndim)
print("No. of values in DataFrame ",df.size)
print("No. of rows and columns is ",df.shape)