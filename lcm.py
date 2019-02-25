print("Enter two numbers to calculate LCM ")
a=int(input("Enter first number "))
b=int(input("Enter second number "))

for m in range (1, a *b +1):
    if m%a ==0 and m%b ==0 :
        print("LCM of number is ", m)
        break
