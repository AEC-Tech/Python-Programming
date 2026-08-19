
# Program to find greatest of three numbers

n1 = int(input("Enter First Number : "))
n2 = int(input("Enter First Number : "))
n3 = int(input("Enter First Number : "))

if n1 > n2 and n1 > n3:
    print(n1," is greatest")

if n2 > n1 and n2 > n3:
    print(n2," is greatest")

if n3 > n2 and n3 > n1:
    print(n3," is greatest")
