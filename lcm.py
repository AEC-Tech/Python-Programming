a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
for i in range( 1, a*b+1 ):
    if i % a == 0 and i % b == 0:
        print("L.C.M. is ",i)
        break
