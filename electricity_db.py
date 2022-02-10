import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="kabir@2211"
  )

connect()
c1 = db1.cursor()
#c1.execute("drop database electricity")
c1.execute("create database electricity")
c1.execute("use electricity")
c1.execute("create table users (username varchar(30), passw varchar(30))")
c1.execute("insert into users values('Anjali','abc123')")
c1.execute("insert into users values('Rahul','xyz123')")
c1.execute("insert into users values('Aarav','pqr123')")
db1.commit()
c1.execute("create table customer(cid varchar(20),name varchar(50),address varchar(50),email varchar(50), phone varchar(20), meterno varchar(20))")
c1.execute("create table bill(meterno varchar(20),billdate date,current_units integer,previous_units integer,consumed integer,amount integer,duedate date,paid varchar(20))")


db1.commit()

