a=input("Enter a string ")
rev=""
for ch in a:
    rev=ch+rev
print("Reverse of string is ", rev)

if a==rev:
    print("String is a Pallindrome")
else:
    print("String is not a Pallindrome")
