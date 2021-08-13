f = open("sample.txt","r")
data = f.readlines()
for line in data:
    for ch in line:
        if ch == ' ':
            print('#',end='')
        else:
            print(ch,end='')
f.close()