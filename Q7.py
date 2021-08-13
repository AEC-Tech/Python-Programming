import csv
def createFile():
    f = open("users.csv","w")
    cw = csv.writer(f)
    cw.writerow(['darsh','coder'])
    cw.writerow(['anjali','coding'])
    cw.writerow(['somya','csv'])
    f.close()
createFile()
un = input("Enter the user name : ")
with open("users.csv","r") as f:
    cr = csv.reader(f)
    for data in cr:
        if data[0] == un:
            print("Found ", data[1])
            break
    else:
        print("Not found")