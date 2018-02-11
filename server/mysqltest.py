from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
class fetching_data():
    def query_with_fetchone(self,data):
        try:
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product")
            a=[]
            b=[]
            c=[]
            d=[]
            data=int(data)
            for row in cursor:
                a.append(row[0])
                b.append(row[1])
                c.append(row[2])
                d.append(row[3])    
            data=str(data)
            for i in range(len(a)):
                if data==a[i]:
                    #cursor.execute("""INSERT INTO selected_item VALUES (%s, %s, %s, %s)""", (a[i],b[i],c[i],d[i]))
                    #conn.commit()
                    return a[i],b[i],c[i],d[i]    
     
        except Error as e:
            print(e)
     
        finally:
            cursor.close()
            conn.close()
    def connect(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM selected_item")
        a=[]
        b=[]
        c=[]
        d=[]
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
        cursor.close()
        conn.close()
        return a,b,c,d
    def delete(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM selected_item")
        a=[]
        b=[]
        c=[]
        d=[]
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
        sum1=0    
        for i in range(len(a)):
            cursor.execute("DELETE FROM selected_item WHERE p_id LIKE '%s'" %(a[i]))
            c[i]=int(c[i])
            sum1=c[i]+sum1
            conn.commit()
            cursor.execute("DELETE FROM product WHERE p_id LIKE '%s'" %(a[i]))
            conn.commit()
            print "deleted"      
        cursor.close()
        conn.close()
        return sum1
    def delete2(self,x):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        a=[]
        b=[]
        c=[]
        d=[]
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
        if len(a)==0:
            return "no"
        for i in range(len(a)):
            cursor.execute("DELETE FROM product WHERE p_id LIKE '%s'" %(x))
            conn.commit()
            print "deleted"      
        cursor.close()
        conn.close()

    def update(self,x):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        a=[]
        b=[]
        c=[]
        d=[]
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
        for i in range(len(a)):
            if a[i]==x[0]:
                cursor.execute("""UPDATE product SET p_name = %s ,price = %s ,description = %s WHERE p_id= %s """,(x[1],x[2],x[3],x[0]))
                conn.commit()
            else:
                return "no"
        cursor.close()
        conn.close()
        
    def insert(self,x):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO selected_item VALUES (%s, %s, %s, %s)""", (x[0],x[1],x[2],x[3]))
        conn.commit()
    def insert2(self,x):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO product VALUES (%s, %s, %s, %s)""", (x[0],x[1],x[2],x[3]))
        conn.commit()    

    def search(self,data):
        try:
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product")
            a=[]
            b=[]
            c=[]
            d=[]
            for row in cursor:
                a.append(row[0])
                b.append(row[1])
                c.append(row[2])
                d.append(row[3])    
            data=str(data)
            for i in range(len(a)):
                if data==b[i]:
                    x=[a[i],b[i],c[i],d[i]]
                    return x    
            return "no" 
        except Error as e:
            print(e)
     
        finally:
            cursor.close()
            conn.close()
            
    def check(self):
        try:
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product")
            stock=[]
            a=[]
            b=[]
            c=[]
            d=[]
            for row in cursor:
                a.append(row[0])
                b.append(row[1])
                c.append(row[2])
                d.append(row[3])    
            for i in range(len(a)):
                counts=0
                for j in range(len(a)):
                    if b[i]==b[j]:
                        counts+=1
                if counts<4:
                    stock.append((b[i],c[i],d[i],counts))
            stock=set(stock)
            return stock
        except:
            pass
     
    def display(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        a=[]
        b=[]
        c=[]
        d=[]
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])    
        return a,b,c,d
        
