import random
import time
print("*"*32)
print("Welcome to Number Guessing Game")
print("*"*32)
k = input("Press a key when ready ")
print("Think of a number from 1 to 50")
k = input("Press a key once done")
print("Double the number you thought of ")
k = input("Hit a key once done")
num = random.randrange(30,101,10)
print("Add", num,"to it and , \nHalf the sum and \ndeduct the number you initially thought of ")
print("Processing",end='')
for i in range(15):
    print(".",end='')
    time.sleep(1)
print("\n")
print("*"*32)
print("You are left with ", num //2 ," !!!!")
print("*"*32)