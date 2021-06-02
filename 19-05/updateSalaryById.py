import sqlite3

con=sqlite3.connect("test.db")
print("opened")

cursor=con.execute('select id from company')

ids=0
for i in cursor:
    ids+=1

print("Total records in table : ",ids)
n=input("Enter Id to be updated")
sal=input("Enter new salary of employee")
      
con.execute("update company set salary="+sal+" where id="+n)

con.commit()
print("Total rows updated",con.total_changes)



    

            
            
