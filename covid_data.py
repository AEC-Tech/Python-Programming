import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="root"
  )

connect()
c1 = db1.cursor()
c1.execute("drop database Covid_Vac")
c1.execute("create database Covid_Vac")
c1.execute("use Covid_Vac")
c1.execute("create table users (username varchar(30), passw varchar(30))")
c1.execute("insert into users values('Anjali','abc123')")
c1.execute("insert into users values('Rahul','xyz123')")
c1.execute("insert into users values('Aarav','pqr123')")
db1.commit()
c1.execute("create table member(aadharno varchar(20),name varchar(50),address varchar(50),email varchar(50), phone varchar(20), age varchar(2))")
c1.execute("create table vaccination(aadharno varchar(20),vname varchar(50),dose1 date, dose2 date)")

db1.commit()

