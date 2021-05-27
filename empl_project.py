import pandas as pd
while True:
    print("Press A - Add a New Employee")
    print("Press B - Display a New Employee")
    print("Press C - Search an Employee")
    print("Press D - Exit")
    opt = input("Enter your choice : ")
    if opt == "A":
        eid = int(input("Enter employee id "))
        name = input("Enter employee name ")
        job = input("Enter job ")
        salary = int(input("Enter Salary "))
        df = pd.read_csv("emp.csv")
        n = df.Empid.count()
        df.loc[n] = [eid,name,job,salary]
        df.to_csv("emp.csv",index=False)
        print("Employee Added Successfully")
    elif opt == "B":
        df = pd.read_csv("emp.csv")
        print(df)
    elif opt == "C":
        eid = int(input("Enter Employee Id to be Searched :"))
        df = pd.read_csv("emp.csv")
        res = df[df.Empid == eid]
        if res.empty:
           print("No Employee found with given id")
        else:
          print(res)
    elif opt == "D":
        break
    else:
        print("Invalid Option Selected")
