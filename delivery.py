import csv
import os
def adddelivery():
    f=open("Delivery.csv","a")
    cid=input("Enter the delivery ID:")
    send=input("Enter the sender's name:")
    recv=input("Enter the reciever's name:")
    doford=input("Enter the date of order:")
    dofdel=input("Enter the date of delivery:")
    cost=input("Enter the cost of delivery:")
    details=[cid,send,recv,doford,dofdel,cost]
    cw=csv.writer(f)
    cw.writerow(details)
    print("Details added Sucessfully!!")
    f.close()
def showall():
    f=open("Delivery.csv","r")
    cr=csv.reader(f)
    print("[CID,Sender's Name,Reciever's Name,Date of Order,Date of delivery,Cost]")
    for k in cr:
        print(k)
    f.close()
def dofd():
    f=open("Delivery.csv","r")
    cd=csv.reader(f)
    cod=input("Enter the date of delivery:")
    for k in cd:
        if k[4]==cod:
            print(k)
        else:
            print("No such Delivery Request found!!")
    f.close()
def delete():
    with open("Delivery.csv","r")as f:
        g=open("temp.csv","w")
        cw=csv.writer(g)
        e=input("Enter the Delivery Id:")
        cr=csv.reader(f)
        for d in cr:
            if d[0]!=e:
                cw.writerow(d)
            if d==[]:
                pass
        print("Data deleted sucessfully!!")
    g.close()
    os.rename("temp.csv","Delivery.csv")
while True:
    print("Press 1 - To add a Order")
    print("Press 2 - To see all delivery")
    print("Press 3 - To see a delivery of the particular day")
    print("Press 4 - To delete a delivery")
    print("Press 5 - To Exit")
    a=int(input("Enter your choice:"))
    if a==1:
        adddelivery()
    elif a==2:
        showall()
    elif a==3:
        dofd()
    elif a==4:
        delete()
    else:
        break





    
       