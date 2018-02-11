import sqlite3

class database():
    def create(self):
        try:
            conn = sqlite3.connect('test.db')
            conn.execute('''CREATE TABLE selected_items(p_id INT PRIMARY KEY     NOT NULL,p_name  TEXT,price INT,description TEXT);''')
        except:
            pass
        finally:
                conn.close()
    def insert(self,text):
        conn = sqlite3.connect('test.db')
        conn.execute("INSERT INTO selected_items VALUES (?, ?, ?, ?)", (int(text[0]),text[1],int(text[2]),text[3]))
        conn.commit()
        print"inserted element"
        conn.close()
    def check(self,k2):
        a=[]
        conn = sqlite3.connect('test.db')
        cursor = conn.execute(" SELECT p_id from selected_items ")
        for row in cursor:
            a.append(row[0])
        print a 
        k2=int(k2)   
        for i in range(len(a)):
            if int(a[i])==k2:    
               conn.execute("DELETE FROM selected_items WHERE p_id= '%s'" % k2)
               conn.commit()
               conn.close()
               print"deleted item"
               return 'yes'      
        conn.close()
        return 'no'              
                           
                       
                       
                       

        
