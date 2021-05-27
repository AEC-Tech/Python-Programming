binary = input("Enter the binay number : ")
s = 0
n = len(binary) - 1
for d in binary:
    s += int(d) * 2 ** n
    n -= 1
print("Decimal is ",s)