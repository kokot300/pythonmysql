import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='abcabc')

if conn.is_connected():
    print("connected")

conn.close()