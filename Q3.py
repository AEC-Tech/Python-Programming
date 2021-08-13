import os
f = open("sample.txt","r")
g = open("temp.txt","w")
res = open("result.txt","w")
data = f.readlines()
for line in data:
    if 'a' in line:
        res.write(line)
    else:
        g.write(line)
f.close()
res.close()
g.close()
os.rename("temp.txt","sample.txt")
print("Done")