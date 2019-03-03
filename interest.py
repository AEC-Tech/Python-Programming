P=int(input("Enter principal amount "))
R=float(input("Enter Rate of interest "))
T=float(input("Enter time in years "))

Si= P * R * T / 100

Ci = P * ((1 + R/100) ** T) - P

print("Simple Interest is ",Si)
print("Compound Interest is ",Ci)
