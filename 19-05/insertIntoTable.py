import sqlite3

con=sqlite3.connect("test.db")
print("opened")

cursor=con.execute('select id from company')

ids=0
for i in cursor:
    ids+=1


con.execute("insert into company(id,name,age,address,salary) values("+str(ids+1)+",'Yash',20,'Hyd',5000.0)")
con.execute("insert into company(id,name,age,address,salary) values("+str(ids+2)+",'Raj',20,'Nlr',45000.0)")
con.execute("insert into company(id,name,age,address,salary) values("+str(ids+3)+",'Sam',20,'Vjd',75000.25)")
con.execute("insert into company(id,name,age,address,salary) values("+str(ids+4)+",'Jack',20,'RR',17500.50)")

con.commit()
print("Total rows inserted",con.total_changes)



    

            
            
