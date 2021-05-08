import random
import time
names = ["Bedant","Vaibhav","Nitin","Palak",
         "Bharath","Medhavi","Inesh",
         "Dipender","Pragya","Suddha"]
print("Total number of players ",len(names))
while len(names) > 1:
    n = random.randint(0,len(names)-1)
    print("Student Eliminated is ", names[n])
    names.pop(n)
    time.sleep(2)
print("-"*30)
print("Winner is ",names[0])
print("-"*30)
