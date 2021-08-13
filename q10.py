f = open("sample.txt","r")
lines = f.readlines()
for line in lines:
    for word in line.split():
        print(word[::-1],end = ' ')
    print()
f.close()