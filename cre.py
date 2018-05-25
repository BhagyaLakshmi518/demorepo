import sqlite3
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
qry="create table student(first varchar,lastnam varchar,username varchar,password varchar,gender varchar,regno varchar,dob varchar,pincode number,marks number,email varchar)"
cur.execute(qry)
print("table created")
cur.close()
conn.close()
