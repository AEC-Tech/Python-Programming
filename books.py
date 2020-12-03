import pickle
def createFile():
    bno = int(input("Enter Book number : "))
    name = input("Enter book title : ")
    author = input("Enter author : ")
    price = int(input("Enter price : "))
    bookdata = [bno,name,author,price]
    f = open("books.dat","ab")
    pickle.dump(bookdata, f)
    f.close()

    
def countRec(author):
    f = open("books.dat","rb")
    bk = []
    count = 0
    try:
        while True:
            bk = pickle.load(f)
            if bk[2] == author:
                count += 1
                print(bk)
    except EOFError:
        f.close()
        print("Number of books written by ",author," is", count)


def updateBook(bid,ncost):
    f = open("books.dat","rb+")
    bk = []
    count = 0
    try:
        while True:
            pos = f.tell()
            bk = pickle.load(f)
            if bk[0] == bid:
                bk[3] = ncost
                f.seek(pos)
                pickle.dump(bk,f)
    except EOFError:
        f.close()
        
def displayBooks():
    f = open("books.dat","rb")
    bk = []
    print("Books available are ")
    try:
        while True:
            
            bk = pickle.load(f)
            print(bk)
    except EOFError:
        f.close()

displayBooks()
updateBook(15,120)
displayBooks()
#n= int(input("How many books are to be added : "))
#for a in range(n):
 #   createFile()

#countRec("Anjali")
    
