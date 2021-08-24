import pandas as pd
nl = [[1,2,3],[5,6,7],[11,44,55]]
df = pd.DataFrame(nl,columns=['Col1','Col2','Col3'],index=['r1','r2','r3'])
print(df)