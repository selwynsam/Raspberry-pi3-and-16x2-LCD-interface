from Tkinter import *
import main
import os
import tkMessageBox
from PIL import ImageTk
from PIL import Image

class log:
    def begin(self,c):    
        fields = 'USER NAME','PASSWORD'
        def fetch(entries):
            save=[]
            for entry in entries:
              field = entry[0]
              text  = entry[1].get()
              save.append(text)
            if save[0]=='admin' and save[1]=='admin':
              tkMessageBox.showinfo("Login","Login Successful")  
              import i2
              c=1
              a=i2.display()
              root.withdraw()
              a.begin(c)
            else:
              tkMessageBox.showinfo("Login failed","wrong  login details") 
                

        def makeform(root, fields):
           entries = []
           for field in fields:
              row = Frame(root)
              lab = Label(row, width=15, text=field, anchor='w')
              lab.config(font=("Courier", 20))
              ent = Entry(row,width=15,font=("Courier", 20))
              row.pack(side=TOP, fill=X, padx=80, pady=20)
              lab.pack(side=LEFT)
              ent.pack(side=RIGHT, expand=YES, fill=X)
              entries.append((field, ent))
           return entries

        if c==0:
            root = Tk()
        if c==1:
            root=Toplevel()
        root.minsize(width=640, height=480)
        image1=Image.open("images/image6.jpg")
        image2=ImageTk.PhotoImage(image1)
        b_label=Label(root,image=image2)
        b_label.place(x=0,y=0,relwidth=1,relheight=1)
        ents = makeform(root, fields)
        root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
        b1 = Button(root, text='LOGIN', command=(lambda e=ents: fetch(e)),height = 3, width =13)
        b1.pack(side=LEFT, padx=200, pady=10)
        b2 = Button(root, text='QUIT', command=root.quit,height = 3, width =13)
        b2.pack(side=LEFT, padx=0, pady=5)
        root.mainloop()
