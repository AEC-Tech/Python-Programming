import pickle
def createFile():
    f = open("emp.dat","ab")
    n = int(input("How many employees : "))
    for i in range(n):
        en = int(input("Enter employee id : "))
        name = input("Enter name : ")
        sal = int(input("Enter Salary : "))
        e ={"Eid":en,"Name":name,"Salary":sal}
        pickle.dump(e,f)
    f.close()

def showFile():
    f = open("emp.dat","rb")
    try:
        while True:
            e = pickle.load(f)
            print(e)
    except:
        f.close()

def showSalary():
    f = open("emp.dat","rb")
    try:
        while True:
            e = pickle.load(f)
            if e['Salary'] >= 25000:
                print(e)
    except:
        f.close()

createFile()
print("List of All Employees ")
showFile()
print("list of Employees earning more than 250000")
showSalary()