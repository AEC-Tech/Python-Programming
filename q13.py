import pickle
def createFile():
    f = open("result.dat","ab")
    n = int(input("How many students to add "))
    for i in range(n):
        rollno = int(input("Enter the roll no : "))
        name = input("Enter the name : ")
        marks = int(input("Enter marks : "))
        pickle.dump([rollno,name,marks],f)
    f.close()

def showScholors():
    f = open("result.dat", "rb")
    try:
        while True:
            st = pickle.load(f)
            if st[2] >= 80:
                print(st[0] , "\t\t",st[1],"\t\t",st[2])
    except:
        f.close()


createFile()
showScholors()