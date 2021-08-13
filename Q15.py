import random
import time

names = []
for i in range(10):
    n = input("Enter a name : ")
    names.append(n)

p = 9
for i in range(9):
    n = random.randint(0,p)
    r = names.pop(n)
    time.sleep(5)
    print("-" * 20)
    print(r ," Eliminated")
    print("-" * 20)
    p -= 1

print("\n\n")
print("-" * 20)
print("Winner is ",names[0])
print("-" * 20)