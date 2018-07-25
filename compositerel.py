R1={}
R2={}
R3={}

n=int(input("Enter the number of elements in first set of relations "))
for i in range(n):
    a=int(input("Enter first value"))
    b=int(input("Enter second value"))
    R1[a]=b

m=int(input("Enter the number of elements in second set of relations "))
for i in range(m):
    a=int(input("Enter first value"))
    b=int(input("Enter second value"))
    R2[a]=b

for x in R1.keys():
    if R1[x] in R2.keys():
        R3[x]=R2[R1[x]]

print(R1)
print(R2)
print(R3)