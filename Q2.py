f = open("sample.txt","r")
vow = 0
cons = 0
upr = 0
lwr = 0
data = f.read()
for ch in data:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vow += 1
        else:
            cons += 1
        if ch.isupper():
            upr += 1
        else:
            lwr += 1

f.close()
print("No. of vowels ",vow)
print("No. of Consonants ",cons)
print("No. of Uppercase letters ",upr)
print("No. of Lowercase letters ",lwr)