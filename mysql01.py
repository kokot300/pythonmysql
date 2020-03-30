import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='abcabc')

if conn.is_connected():
    print("connected")

cursor=conn.cursor()
cursor.execute('select * from emp')

try:
    cursor.execute('insert into emp values(3,'joe',30000)')
    cursor.commit()
    print("employee added")
except:
    conn.rollback()

#row=cursor.fetchone() #fetch one with while or fetch all with for
row=cursor.fetchall()
print("total no of records ", cursor.rowcount)

for row in rows:
    print(row)
#while row is not None:
#    print(row)
#    row=cursor.fetchone()

cursor.close()
conn.close()