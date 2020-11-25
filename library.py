import pandas as pd
def addNewBook():
    bookid = int(input("Enter a book id : "))
    title = input("Enter book title : ")
    author = input("Enter author of the book : ")
    publisher = input("Enter book publisher : ")
    edition = input("Enter edition of book : ")
    cost = int(input("Enter cost of the book : "))
    category = input("Enter category of book : ")
    bdf = pd.read_csv("books.csv")
    n = bdf["bookid"].count()
    bdf.at[n] = [bookid,title,author,publisher,edition,cost,category]
    bdf.to_csv("books.csv",index = False)
    print("Book added successfully")

def login():
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")
    df = pd.read_csv("users.csv")
    df = df.loc[df["username"] == uname]
    if df.empty:
        print("Invalid Username given")
        return False
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True


def showMenu():
    print("-----------------------------")
    print("       ABC LIBRARY MGT       ")
    print("-----------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - To view Charts")
    choice = int(input("Enter your choice : "))
    return choice

if login():
    ch = showMenu()
    if ch == 1:
        addNewBook()
