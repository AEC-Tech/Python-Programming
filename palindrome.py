text = input("Enter the string to be checked : ")

#rev=""
#n = len(text)
#for a in range(n-1, -1, -1):
    #rev += text[a]

rev = text[::-1]

print("Reverse of string is ", rev)

if text == rev:
    print(text," is a Palindrome")
else:
    print(text," is not a palindrome")
