def process(A):
    for i in range(len(A)):
        if i % 2 == 0:
            A[i] *= 2
        else:
            A[i] /= 2


N = [10,21,30]
print(N)
process(N)
print(N)