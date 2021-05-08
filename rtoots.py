import math
a = float(input("Enter a "))
b = float(input("Enter b "))
c = float(input("Enter c "))
d = b ** 2 - 4 * a * c
if d == 0:
    print("Equal real roots")
    r = -b/ (2 * a)
    print("Root Value",r)
elif d < 0:
    print("No Real roots")
else:
    r1 = (-b + math.sqrt(d))/ (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are ",r1,r2)
