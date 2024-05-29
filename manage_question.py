from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import add_question
import db.db

class manage_question:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=1200,height=400,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-1200/2)
        y=int(height/2-400/2)
        
        str1 = "1200x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Manage Question")
    def add_frame(self):
        self.frame=Frame(self.win,width=1100,height=300)
        self.frame.place(x=80,y=20)
        x,y=70,20
        self.tr = Treeview(self.frame,columns=('A','B','C','D','E','F','G','H','I'),selectmode="extended")
        self.tr.heading('#0',text='Sr No')
        self.tr.column('#0',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#1',text='Category')
        self.tr.column('#1',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#2',text='Question')
        self.tr.column('#2',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#3',text='Option1')
        self.tr.column('#3',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#4',text='Option2')
        self.tr.column('#4',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#5',text='Option3')
        self.tr.column('#5',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#6',text='Option4')
        self.tr.column('#6',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#7', text='Answer')
        self.tr.column('#7', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#8',text='Edit')
        self.tr.column('#8',minwidth=0,width=100,stretch=NO)
        self.tr.heading('#9',text='Delete')
        self.tr.column('#9',minwidth=0,width=100,stretch=NO)

        j=0
        for i in db.db.manage_question():
            self.tr.insert('',index=j,text=i[0],value=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],'Edit','Delete'))
            j+=1
        self.tr.bind('<Double-Button-1>',self.actions)
        self.tr.place(x=50,y=y+50)
        self.win.mainloop()

        self.win.mainloop()


    def actions(self, e):
        tt = self.tr.focus()

        col = self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        tup = (
          self.tr.item(tt).get('text'),

        )

        if col == '#9':
            res = messagebox.askyesno("Message", "Do you want to delete")
            if res:
                rs = db.db.delete_question(tup)
            if rs:
                 messagebox.showinfo("Message", "data deleted successfully")
                 self.win.destroy()
                 z = manage_question()
                 z.add_frame()
            else:
                self.win.destroy()
                z = manage_question()
                z.add_frame()

        elif col == '#2':
             res = add_question.add_question(self.tr.item(tt))
             self.win.destroy()
             res.add_frame()

