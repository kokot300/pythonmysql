import mysql.connector

def delete(id)
    conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='abcabc')

    if conn.is_connected():
        print("connected")
        cursor=conn.cursor()
        args=(id)
        str="delete from emp where id='%id'"

    try:
        cursor.execute(str % args)
        cursor.commit()
        print("employee deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

empID=int(input("enter id:\n"))
deelte(empID)