n=int(input("How many direct flights are there "))
flight=[]
for i in range(n):
    source=int(input("Enter the source city number "))
    dest=int(input("Enter the destination city number "))
    flight.append((source,dest))

print(flight)

onehop=[]
for x in flight:
    for y in flight:
        if x[1]==y[0]:
            onehop.append((x[0],y[1]))

print(onehop)