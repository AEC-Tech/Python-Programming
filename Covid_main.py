import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="root",
    database = "Covid_Vac"
  )
  

def showusers():
    c1 = db1.cursor()
    c1.execute("select * from users")
    res = c1.fetchall()
    #print(res)
    print("List of Users ")
    for val in res:
        print("UserName = "+val[0] + " Password = " + val[1])

def login():
    print("-" * 50)
    print("\t COVID VACCINATION RECORD")
    print("-" * 50)
    print("\t LOGIN")
    un = input("Enter User Name : ")
    pw = input("Enter Password : ")
    q = "select * from users where username = %s and passw = %s"
    val = (un,pw)
    c2 = db1.cursor()
    c2.execute(q,val)
    res = c2.fetchall()
    print("-" * 50)
    if len(res) == 0:
        print("Invalid User Name or Password ")
        print("-" * 50)
        return False
    else:
        print("Access Granted !!!")
        print("-" * 50)
        return True
def addmember():
    ad = input("Enter Aadhar card no. : ")
    name = input("Enter Member Name : ")
    addr = input("Enter Address : ")
    phone = input("Enter Phone Number : ")
    email = input("Enter Email :")
    age = input("Enter Age of member : ")
    cursor1 = db1.cursor()
    q = "insert into member values (%s,%s,%s,%s,%s,%s)"
    val = (ad,name,addr,phone,email,age)
    cursor1.execute(q,val)
    db1.commit()
    print("Member Added Successfully")

def showmembers():
    c1 = db1.cursor()
    c1.execute("select * from member")
    res = c1.fetchall()
    #print(res)
    print("List of Members ")
    for val in res:
        print("Name = "+val[1] + " Aadhar Card= " + val[0])

def addvaccination():
    ad = input("Enter Aadhar card no. : ")
    name = input("Enter Vaccination Name : ")
    d = input("Enter 1 for Dose 1 , 2 for Dose 2 : ")
    dt = input("Enter the date of Vaccination : ")
    c2 = db1.cursor()
    if d == "1":
        q = "insert into vaccination values(%s,%s,%s,NULL)"
        val = (ad,name,dt)
        c2.execute(q,val)
        db1.commit()
        print("Vaccination Record Added Successfully")
    elif d == "2":
        q = "update vaccination set dose2=%s where aadharno=%s"
        val =(dt,ad)
        c2.execute(q,val)
        db1.commit()
        print("Vaccination Record Updated Successfully")
    else:
        print("Invalid Input, please try again")
        
def showvaccin():
    c1 = db1.cursor()
    c1.execute("select * from vaccination,member where vaccination.aadharno=member.aadharno")
    res = c1.fetchall()
    #print(res)
    print("List of Vaccinated Members ")
    print("-"*40)
    print("Name\tVaccine\tAadhar No\tDose1\tDose2")
    print("-"*40)
    for val in res:
        print(val[5],"\t",val[1] , "\t" , val[0],"\t",val[2],"\t",val[3])
        
def shownotvaccinated():
    c1 = db1.cursor();
    c1.execute("Select * from member where aadharno not in (select aadharno from vaccination)")
    res = c1.fetchall()
    print("List of Not Vaccinated Members ")
    print("-"*40)
    print("Name\tAadhar No\tPhone\tAddress\tEmail")
    print("-"*40)
    for val in res:
        print(val[1],"\t",val[0] ,"\t",val[3],"\t",val[2],"\t",val[4])
        
def showduevaccine():
    c1 = db1.cursor()
    c1.execute("select * from vaccination,member where vaccination.aadharno=member.aadharno and dose2 is null")
    res = c1.fetchall()
    #print(res)
    print("List of Members Whose Dose2 is due ")
    print("-"*40)
    print("Name\tVaccine\tAadhar No\tDose1\tDose2")
    print("-"*40)
    for val in res:
        print(val[5],"\t",val[1] , "\t" , val[0],"\t",val[2],"\t",val[3])

    



connect()
print("Connected")
if login():
    while True:
        print("-" * 50)
        print("\t CHOOSE AN OPERATION ")
        print("-" * 50)
        print("Press 1 - Add a New Society Member")
        print("Press 2 - Add a Vaccination Record")
        print("Press 3 - Show all Members")
        print("Press 4 - Show All Vaccinated Members")
        print("Press 5 - Show Whose Vaccination is Due")
        print("Press 6 - Show Who are not at all Vaccinated")
        print("Press 7 - Quit")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            addmember()
        elif ch == 2:
            addvaccination()
        elif ch == 3:
            showmembers()
        elif ch == 4:
            showvaccin()
        elif ch == 5:
            showduevaccine()
        elif ch == 6:
            shownotvaccinated()
        elif ch == 7:
            break
    

