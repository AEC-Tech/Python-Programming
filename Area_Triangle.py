import math
a=float(input("Enter first side of the triangle "))
b=float(input("Enter second side of the triangle "))
c=float(input("Enter third side of the triangle "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is ",area)
