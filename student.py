names=[]
marks=[]
for i in range(5):
    n=input("Enter student name ")
    m=int(input("Enter marks of student "))
    names.append(n)
    marks.append(m)
h=max(marks)
l=min(marks)
print("Highest marks are ",h)
print("Lowest marks are ",l)
for i in range(5):
    if h == marks[i]:
        print("Student having highest marks is ",names[i])
    if l==marks[i] :
        print("Student having lowest marks is ", names[i])
