import csv
import os
def createFile():
    n = int(input("How many students to add : "))
    f = open("stu.csv","a")
    cw = csv.writer(f)
    for i in range(n):
        admno = input("Enter admission no : ")
        name = input("Enter name : ")
        cls = input("Enter Class : ")
        s = [admno,name,cls]
        cw.writerow(s)
    f.close()

def display():
    with open("stu.csv","r") as f:
        cr = csv.reader(f)
        for s in cr:
            print(s)
def search():
    ad = input("Enter admission no to be searched : ")
    with open("stu.csv","r") as f:
        cr = csv.reader(f)
        for s in cr:
            if s[0] == ad:
                print(s)
                break
        else:
            print("No student found with given admission no")

def remove():
    ad = input("Enter admission no to be deleted : ")
    with open("stu.csv","r") as f:
        cr = csv.reader(f)
        t = open("temp.csv","w")
        cw = csv.writer(t)
        for s in cr:
            if s[0] == ad:
                print(s)
            else:
                cw.writerow(s)
        t.close()
        os.remove("stu.csv")
        os.rename("temp.csv","stu.csv")
def update():
    ad = input("Enter admission no to be updated : ")
    with open("stu.csv","r") as f:
        cr = csv.reader(f)
        t = open("temp.csv","w")
        cw = csv.writer(t)
        for s in cr:
            if s[0] == ad:
                print("Old data is ",s)
                s[1] = input("Enter modified name : ")
                s[2] = input("Enter modified class : ")
                cw.writerow(s)
            else:
                cw.writerow(s)
        t.close()
        os.remove("stu.csv")
        os.rename("temp.csv","stu.csv")

while True:
    print("-" * 30)
    print("Press 1 - Add New Students")
    print("Press 2 - Display All Students")
    print("Press 3 - Search a Student")
    print("Press 4 - Delete a Student")
    print("Press 5 - Update a Student")
    print("Press 6 - Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        createFile()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        remove()
    elif ch == 5:
        update()
    elif ch == 6:
        break