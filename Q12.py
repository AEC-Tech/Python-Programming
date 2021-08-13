f = open("sample.txt","r")
dg = 0
data = f.read()
for ch in data:
    if ch.isdigit():
        dg += 1

f.close()
print("No. of digits ",dg)
