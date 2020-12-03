text = input("Enter some text ")
count_letters = len(text)
count_words = len(text.split(" "))
count_alpha = 0
count_digit = 0
count_space = 0
count_special = 0

for ch in text:
    if ch.isalpha():
        count_alpha += 1
    elif ch.isdigit():
        count_digit += 1
    elif ch.isspace():
        count_space += 1
    else:
        count_special += 1
        


print("Total no. of characters ",count_letters)
print("Total no. of words ",count_words)
print("Total no. of alphabets ",count_alpha)
print("Total no. of digits ",count_digit)
print("Total no. of spaces ",count_space)
print("Total no. of special characters ",count_special)



