count = 0
for i in range(10):
    num = int(input("Enter a number "))
    if num % 10 == 7:
        count += 1
print("Number of values having 7 as last digit ", count)
