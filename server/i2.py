from Tkinter import *
import login
import main
from PIL import ImageTk
from PIL import Image
class display():
    def begin(self,c):
        def dtbase():
            import database
            a=database.display1()
            root2.withdraw()
            a.begin()
            
        def check1():
            import stock_check
            a=stock_check.display()
            a.begin()
            return
        def bill():
            import interface
            a=interface.display()
            a.begin()
            return
        def edit():
            a=main.display()
            root2.withdraw()
            a.login()
        def Logout():
            root2.withdraw()
            print"successful logout"
            import login
            a=login.log()
            c=1
            a.begin(c)
            
        if c==0:
            root2 = Tk()
        if c==1:
            root2=Toplevel()
        root2.minsize(width=640, height=480)
        image1=Image.open("images/image1.jpg")
        image2=ImageTk.PhotoImage(image1)
        b_label=Label(root2,image=image2)
        b_label.place(x=0,y=0,relwidth=1,relheight=1)
        b1 = Button(root2, text='CHECK STOCK', command=check1,height = 2, width =15)
        b1.pack(side=TOP, padx=200, pady=20)
        b1.config(font=("Courier", 20))
        b2 = Button(root2, text='BILLING', command=bill,height = 2, width =15)
        b2.pack(side=TOP, padx=200, pady=20)
        b2.config(font=("Courier", 20))
        b3 = Button(root2, text='EDIT RECORDS', command=edit,height = 2, width =15)
        b3.pack(side=TOP, padx=200, pady=20)
        b3.config(font=("Courier", 20))
        b4 = Button(root2, text='DATABASE', command=dtbase,height = 2, width =15)
        b4.pack(side=TOP, padx=200, pady=20)
        b4.config(font=("Courier", 20))
        b5 = Button(root2, text='LOGOUT', command=Logout,height = 2, width =15)
        b5.pack(side=TOP, padx=200, pady=20)
        b5.config(font=("Courier", 20))
        root2.mainloop()
