n=int(input("How many rows are there "))
for a in range (n, 0, -1):
    for b in range (n, a-1,-1):
        print(b, end=' ')
    print()
