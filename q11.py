'''
Interchange the first half of a list with second half
eg A = [70,90,60,80,50,20]
output = [80,50,20,70,90,60
'''

def swap(A):
    n = len(A)
    for i in range(n//2):
        temp = A[i]
        A[i] = A[i+n//2]
        A[i+n//2] = temp

A = [70,90,60,80,50,20]
print(A)
swap(A)
print(A)