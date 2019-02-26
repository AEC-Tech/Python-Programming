print("Calculating Average of N numbers ")
n=int(input("How many numbers are there "))
nums=[]
for i in range (n):
    a=int(input("Enter a number "))
    nums.append(a)

avg=sum(nums)/n
print("Average of numbers is ",avg)



