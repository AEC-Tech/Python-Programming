import pickle
def createFile():
    f = open("student.dat","ab")
    n = int(input("How many students to add "))
    for i in range(n):
        rollno = int(input("Enter the roll no : "))
        name = input("Enter the name : ")
        pickle.dump([rollno,name],f)
    f.close()

def showFile():
    f = open("student.dat", "rb")
    try:
        while True:
            st = pickle.load(f)
            print(st[0] , "\t\t",st[1])
    except:
        f.close()


createFile()
f = open("student.dat","rb")
rn = int(input("Enter rollno to be searched "))
found = False
try:
    while True:
        st = pickle.load(f)
        if st[0] == rn:
            print("Found ",st[1])
            found = True
            break
except:
    f.close()
    if found == False:
        print("Roll no not found")
showFile()