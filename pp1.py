import pandas as pd
pdict = {"P_Id":[108,109,110,111,112, 113],
         "Name":['Faizal','Harish','Surinder','Punit','Geet','Tarun'],
         "Bill":[1200,25000,1500,1300,2000,24000]}
df = pd.DataFrame(pdict)
df.sort_values(by='Bill',ascending=False, inplace=True)
print(df)
df.set_index('P_Id',inplace=True)
df['Date']=['12/3/1990','18/3/1990']
print(df)
