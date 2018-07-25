dict1={'admno':1234,'name':'Ankit','course':'B.C.A.','semester':5}
print("Admission no. is ", dict1['admno'])
print("Name is ",dict1['name'])
print("Course Taken is ",dict1['course'])
print("Semester is ",dict1['semester'])

number={1:'One',2:'Two',3:'Three'}
#n=int(input("Enter a number "))
#print(number[n])

for x in dict1.keys():
    print(x, " => ",dict1[x])