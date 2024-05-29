from tkinter import *
from tkinter.ttk import Treeview
import db.db
import tkinter
from tkinter import messagebox
import add_register

class manage_users:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=900,height=400,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-900/2)
        y=int(height/2-400/2)
        
        str1 = "900x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Manage Users")
    def add_frame(self):
        self.frame=Frame(self.win,width=800,height=300)
        self.frame.place(x=80,y=20)
        x,y=70,20
        self.tr = Treeview(self.frame,columns=('A','B','C','D','E','F'),selectmode="extended")
        self.tr.heading('#0',text='Sr No')
        self.tr.column('#0',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#1',text='Name')
        self.tr.column('#1',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#2',text='Email')
        self.tr.column('#2',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#3',text='Contact')
        self.tr.column('#3',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#4',text='Gender')
        self.tr.column('#4',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#5',text='Edit')
        self.tr.column('#5',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#6',text='Delete')
        self.tr.column('#6',minwidth=0,width=100,stretch=NO)


        j=0
        for i in db.db.manage_users():
            self.tr.insert('',index=j,text=i[0],value=(i[1],i[2],i[3],i[4],'Edit','Delete'))
            j+=1

        self.tr.place(x=50,y=y+50)
        self.tr.bind('<Double-Button-1>',self.actions)

        self.win.mainloop()

    def actions(self, e):
        tt=self.tr.focus()

        col=self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        tup=(
            self.tr.item(tt).get('text'),
        )

        if col=='#6':
            res= messagebox.askyesno("Message","Do you want to delete")
            if res:
                rs=db.db.delete_users(tup)
                if rs:
                     messagebox.showinfo("Message","data deleted successfully")
                     self.win.destroy()
                     z=manage_users()
                     z.add_frame()
                else:
                    self.win.destroy()
                    z = manage_users()
                    z.add_frame()

        # elif col =='#2':
        #     res = add_register.users_register(self.tr.item(tt))
        #     self.win.destroy()
        #     res.add_frame()
