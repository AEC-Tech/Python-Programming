text = input("Enter text ")
print("Original text is ",text)
words = text.lower().split(" ")
for word in words:
    print(word[0].upper(),end='')
    print(word[1:],end = ' ')
