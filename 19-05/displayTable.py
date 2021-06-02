import sqlite3

con=sqlite3.connect("test.db")
print("opened")

cursor=con.execute("select id,name,age,address,salary from company")

for row in cursor:
    print("Id : ",row[0])
    print("Name : ",row[1])
    print("Age : ",row[2])
    print("Addres : ",row[3])
    print("Salary : ",row[4])

con.close()


    

            
            
