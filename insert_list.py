A=[12,34,56,11,24,65,76]
print("List is ",A)
num=int(input("Enter number to be inserted in the list "))
pos=int(input("enter the position to insert the number "))
A.insert(pos,num)
print("Modified list ",A)