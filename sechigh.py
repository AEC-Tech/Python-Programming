L = [78,45,90,66,85,65]
highest = L[0]
for i in L:
    
    if i > highest:
        highest = i
    
print("Highest number is  ", highest)

sh = 0
for i in L:
    
    if i > sh and i != highest:
        sh = i
   
print("Second Highest number is  ", sh)
