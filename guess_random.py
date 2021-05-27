import random

num = random.randint(1,100)
name = input("Enter Player Name ")
for i in range(7):
    val = int(input("Enter the guessed number from 1 to 100 : "))
    if num == val:
        print(name, " Wins !!!")
        break
    elif num < val:
        print("Actual number is less than your Guess")
        print("You can Try Again !!!")
    elif num > val:
        print("Actual number is greater than your Guess")
        print("You can Try Again !!!")
else:
    print(name, " LOOSE !!1")
    print("Actual Number is ",val)