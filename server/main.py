from Tkinter import *
import tkMessageBox
import interface
import mysqltest
import tkMessageBox
from PIL import ImageTk
from PIL import Image

class display():
    def login(self):
        fields = 'P_ID','P_NAME','PRICE','DESCRIPTION'
        def fetch(entries):
            save=[]
            for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              save.append(text)
            if save[0]=='admin' and save[1]=='admin':
              a=interface.display()
              a.login()
        def insert(entries):
            save=[]
            for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              if text=="":
                  tkMessageBox.showinfo("Insert","Incomplete details entered")
                  for entry in entries:
                      entry[1].delete(0, END)    
                  return
              save.append(text)
              entry[1].delete(0, END)
              print field,text
            d=mysqltest.fetching_data()
            d.insert2(save)
            tkMessageBox.showinfo("Insert","Inserted sucessfully")

        def delete(entries):
            save=[]
            for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              save.append(text)
              entry[1].delete(0, END)
              print field,text
            d=mysqltest.fetching_data()
            x=d.delete2(save[0])
            if x=="no":
                tkMessageBox.showinfo("WARNING","No entry to Delete")
            else:    
                tkMessageBox.showinfo("Delete","successful delete")

        def update(entries):
            save=[]
            for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              if text=="":
                  tkMessageBox.showinfo("Update","Incomplete records entered to update")
                  for entry in entries:
                      entry[1].delete(0, END)    
                  return
              save.append(text)
              entry[1].delete(0, END)
              print field,text
            d=mysqltest.fetching_data()
            x=d.update(save)
            if x=="no":
                tkMessageBox.showinfo("WARNING","Update error")
            else:    
                tkMessageBox.showinfo("Update","Update successful")

        def search(entries):
            save=[]
            for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              save.append(text)
              entry[1].delete(0, END)
              print field,text
            if save[1]=="":
                tkMessageBox.showinfo("WARNING","Enter P_name to search")
                return
            print save[1]
            d=mysqltest.fetching_data()
            x=d.search(save[1])
            if x=="no":
                tkMessageBox.showinfo("Search","Search failed")
            else:
                i=0
                for entry in entries:
                  entry[1].insert(0,x[i])
                  i+=1
                tkMessageBox.showinfo("Search","Details found")

        def Logout():
            root2.withdraw()
            print"successful logout"
            import i2
            x=i2.display()
            c=1
            x.begin(c)

        def makeform(root2, fields):
            entries = []
            for field in fields:
              row = Frame(root2)
              lab = Label(row, width=15, text=field, anchor='w')
              lab.config(font=("Courier", 20))
              ent = Entry(row,width=15,font=("Courier", 20))
              row.pack(side=TOP, fill=X, padx=80, pady=20)
              lab.pack(side=LEFT)
              ent.pack(side=RIGHT, expand=YES, fill=X)
              entries.append((field, ent))
            return entries

        root2 = Toplevel() 
        root2.minsize(width=640, height=480)
        image1=Image.open("images/image3.jpg")
        image2=ImageTk.PhotoImage(image1)
        b_label=Label(root2,image=image2)
        b_label.place(x=0,y=0,relwidth=1,relheight=1)
        ents = makeform(root2, fields)
        root2.bind('<Return>', (lambda event, e=ents: fetch(e)))   
        b1 = Button(root2, text='INSERT', command=(lambda e=ents: insert(e)),height = 3, width =13)
        b1.pack(side=LEFT, padx=50, pady=10)
        b2 = Button(root2, text='DELETE', command=(lambda e=ents: delete(e)),height = 3, width =13)
        b2.pack(side=LEFT, padx=0, pady=5)

        b3 = Button(root2, text='UPDATE', command=(lambda e=ents: update(e)),height = 3, width =13)
        b3.pack(side=LEFT, padx=50, pady=10)
        b4 = Button(root2, text='SEARCH', command=(lambda e=ents: search(e)),height = 3, width =13)
        b4.pack(side=LEFT, padx=0, pady=5)
        b5 = Button(root2, text='BACK', command=(lambda e=ents: Logout()),height = 3, width =13)
        b5.pack(side=LEFT, padx=50, pady=5)
        root2.mainloop()
