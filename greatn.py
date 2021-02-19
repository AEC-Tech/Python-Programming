num = int(input("Enter a number "))
highest = lowest = num
for i in range(9):
    num = int(input("Enter a number "))
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num
print("Highest number is  ", highest)
print("Lowest number is  ", lowest)
