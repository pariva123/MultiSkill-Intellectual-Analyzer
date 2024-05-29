from tkinter import *
from tkinter import messagebox
import db.db
import manage_category

class add_category:
    def __init__(self,data=''):
        self.data=data
        print(self.data)
        self.win=Tk()
        self.canvas=Canvas(self.win,width=900,height=600,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-500/2)

        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Add Category")

    def add_frame(self):

        self.frame=Frame(self.win,width=500,height=400)
        self.frame.place(x=60,y=40)

        x,y=70,20


        self.label=Label(self.frame,text="Add Category")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=160,y=y+220)

        self.nmlabel=Label(self.frame,text="Name")
        self.nmlabel.config(font=('times new roman',15,'bold'))
        self.nmlabel.place(x=90,y=y+270)

        self.name=Entry(self.frame)
        self.name.place(x=200,y=y+270)

        if self.data == '':
            self.button=Button(self.frame,text="Submit",font=('times new roman',15,'bold'),bg='white',fg='black',command=self.add)
            self.button.place(x=220,y=y+300)
        else:
            up=dict(self.data).get('values')

            self.name.insert(0,up[0])

            self.button = Button(self.frame, text="update", font=('times new roman', 15, 'bold'), bg='white', fg='black',
                                command=self.update_category)
            self.button.place(x=220, y=y + 300)

        self.win.mainloop()

    def add(self):
        data = (
            self.name.get(),
            'ACTIVE'
            )
        if self.name.get() =="":
            messagebox.showwarning("Alert","enter name first")
        else:
            res = db.db.add_category(data)
            if res:
                messagebox.showinfo("message","success")
                self.win.destroy()
            else:
                messagebox.showerror("alert","something went wrong")
    def update_category(self):
        tup=(
            self.name.get(),
            dict(self.data).get('text')
        )
        print(tup)
        res = db.db.update_category(tup)
        if res:
            messagebox.showinfo("message", "Updated")
            self.win.destroy()
            x = manage_category.manage_category()
            x.add_frame()


if __name__ == "__main__":
    x=add_category()
    x.add_frame()

