import sqlite3

con=sqlite3.connect("test.db")
print("opened")

cursor=con.execute('select id from company')

ids=0
for i in cursor:
    ids+=1

print("Total records in table : ",ids)
n=input("Enter Id to be deleted")
      
con.execute("delete from company where id="+n)

con.commit()
print("Total records deleted ",con.total_changes)



    

            
            
