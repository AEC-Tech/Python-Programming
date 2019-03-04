marks = []
for a in range(5):
    n = int(input("Enter marks in Subject "+ str(a+1) + ": "))
    marks.append(n)
total=sum(marks)
avg=total/5
print("Total Marks are ",total)
print("Percentage Marks are ",avg)
