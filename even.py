L = [78,45,90,66,85,65]

val = L[0]
for i in range(len(L)-1):
    L[i] = L[i+1]

L[-1] = val

print(L)
