import pickle
import os
def createFile():
    f = open("student2.dat","ab")
    n = int(input("How many students to add "))
    for i in range(n):
        rollno = int(input("Enter the roll no : "))
        name = input("Enter the name : ")
        marks = int(input("Enter marks : "))
        pickle.dump([rollno,name,marks],f)
    f.close()

def showFile():
    f = open("student2.dat", "rb")
    try:
        while True:
            st = pickle.load(f)
            print(st[0] , "\t\t",st[1],"\t\t",st[2])
    except:
        f.close()


#createFile()
showFile()
f = open("student2.dat","rb")
g = open("temp.dat","wb")
rn = int(input("Enter rollno to be searched "))
found = False
try:
    while True:
        st = pickle.load(f)
        if st[0] == rn:
            print("Found ",st[1],st[2])
            st[2] = int(input("Enter the updated marks : "))
            print(st)
            pickle.dump(st,g)
            found = True
        else:
            pickle.dump(st,g)
except:
    f.close()
    g.close()
    os.rename("temp.dat","student2.dat")

    if found == False:
        print("Roll no not found")

showFile()