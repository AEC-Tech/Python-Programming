print("Enter two numbers to calculate HCF ")
a=int(input("Enter first number "))
b=int(input("Enter second number "))
while a%b !=0:
    rem=a%b
    a=b
    b=rem

print("HCF is  ", b)