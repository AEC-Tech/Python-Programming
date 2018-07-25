str=input("Enter a string")
print("String is ",str)
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        #count[x]=1
        count.update()

print(count)
for x in count.keys():
    print(x, " occurs for ",count[x]," times")
