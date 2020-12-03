#to calculate the frequency of each alphabet

text = input("Enter the string : ")
count = { }
for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
print(count)


program
{'p':1 ,'r': 2,'o':1,'g':1,'a':1, 'm':1}
