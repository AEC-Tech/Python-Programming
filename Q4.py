import pandas as pd
iprod = { 'Rice': {'AP':600, 'Guj': 700} ,
        'Wheat': {'AP':800, 'Guj': 555} ,
        'Fruits': {'AP':400, 'Guj': 900} }

df = pd.DataFrame(iprod)
print(df)
print("Grain Production")
print(df.loc[:,["Rice","Wheat"]])