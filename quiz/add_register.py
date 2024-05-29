from tkinter import *
from tkinter import messagebox
import users.users_navigation
import db.db


class users_register:
    def __init__(self,data=''):
        self.win=Tk()
        self.data=data
        self.canvas=Canvas(self.win,width=900,height=600,bg='pink')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-500/2)
        
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Login Window")
        
    def add_frame(self):
        
        self.frame=Frame(self.win,width=500,height=400,bg='pink')
        self.frame.place(x=60,y=40)
        
        x,y=70,20
        
        
        self.label=Label(self.frame,text="User Register")
        self.label.config(font=('times new roman',20,'bold'),fg='blue')
        self.label.place(x=160,y=y+0)
        
        self.nmlabel=Label(self.frame,text="Name")
        self.nmlabel.config(font=('times new roman',18,'bold'),fg='blue')
        self.nmlabel.place(x=50,y=y+85)
        self.name=Entry(self.frame,font=('times new roman',12,'bold'),fg='dark red')
        self.name.place(x=200,y=y+85)
        
        self.emlabel=Label(self.frame,text="Email")
        self.emlabel.config(font=('times new roman',18,'bold'),fg='blue')
        self.emlabel.place(x=50,y=y+140)
        self.email=Entry(self.frame,font=('times new roman',12,'bold'),fg='dark red')
        self.email.place(x=200,y=y+140)

        self.cnlabel=Label(self.frame,text="Contact")
        self.cnlabel.config(font=('times new roman',18,'bold'),fg='blue')
        self.cnlabel.place(x=50,y=y+190)
        self.contact=Entry(self.frame,font=('times new roman',12,'bold'),fg='dark red')
        self.contact.place(x=200,y=y+190)

        self.var=StringVar(self.win, 'Male')
        self.gnlabel=Label(self.frame,text="Gender")
        self.gnlabel.config(font=('times new roman',18,'bold'),fg='blue')
        self.gnlabel.place(x=50,y=y+235)

        self.male=Radiobutton(self.frame,variable=self.var,font='bold 15',fg='blue',text='Male',value='Male',command=self.sel)
        self.male.place(x=200,y=y+235)

        self.female = Radiobutton(self.frame, variable=self.var, font='bold 15',fg='blue', text='Female', value='Female',command=self.sel)
        self.female.place(x=270, y=y +235)

        self.cnlabel = Label(self.frame, text="Password")
        self.cnlabel.config(font=('times new roman', 18, 'bold'),fg='blue')
        self.cnlabel.place(x=50, y=y + 290)
        self.password = Entry(self.frame,font=('times new roman',12,'bold'),fg='dark red')
        self.password.place(x=200, y=y + 290)
        
        if self.data == '':
            self.button=Button(self.frame,text="Register",font=('times new roman',18,'bold'),bg='rosy brown',fg='black',command=self.buttonreg)
            self.button.place(x=200,y=y+330)
        else:
            up=dict(self.data).get('values')
            self.name.insert(0,up[0]),
            self.email.insert(0, up[1]),
            self.contact.insert(0, up[2])

            self.button = Button(self.frame,text="UPDATE",font='times new roman',command=self.edit_users)

        self.win.mainloop()

    def buttonreg(self):
        data = (
            self.name.get(),
            self.email.get(),
            self.contact.get(),
            self.var.get(),
            self.password.get()
        )

        if self.name.get() == "":
            messagebox.showinfo("Alert !,enter name first")
        elif self.email.get() == "":
            messagebox.showinfo("Alert !,enter email first")
        elif self.contact.get() == "":
            messagebox.showinfo("Alert !,enter contact first")
        elif self.var.get() == "":
            messagebox.showinfo("Alert !,enter gender first")
        elif self.password.get() == "":
            messagebox.showinfo("Alert !,enter password first")
        else:
            res = db.db.users_register(data)
            if res:
                messagebox.showinfo("message","Register succesfully")
                self.win.destroy()
                
            else:
                messagebox.showinfo("Alert !,something went wrong")
               
    def edit_users(self):
        tup=(
            self.name.get(),
            self.email.get(),
            self.contact.get(),
            self.var.get(),
            dict(self.data).get('text')
        )
        # res = db.db.edit_users(tup)
        # if res:
        #     messagebox.showinfo("message","data updated successfully")
            # self.win.destroy()
            # x= manage_users.manage_users()
            # x.add_frame()

    def sel(self):
        print(self.var.get())


if __name__ == "__main__":
        d = users_register()
        d.add_frame()
