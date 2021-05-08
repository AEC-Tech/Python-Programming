def process(A):
    s = 0
    for k in A:
        if A[k] < 100:
            s = s + A[k]
    print(s)

S = {'A':167,'B':78,'C':92}
print(S)
process(S)
print(S)