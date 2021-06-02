import sqlite3

con=sqlite3.connect("test.db")
print("opened")

con.execute('''create table company(id int primary key not null, 
            name text not null,
            age int not null,
            address char(50),
            salary real);''')

print("created table")



    

            
            
