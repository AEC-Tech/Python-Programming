text = input("Enter the string : ")
count = 0

for ch in text:
    #if ch in "aeiouAEIOU":
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

print("No. of vowels are ",count)


