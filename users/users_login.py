from tkinter import *
from tkinter import messagebox
import users.users_register
import users.users_navigation
import db.db

class users_login:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=900,height=600,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-500/2)
        
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)
        self.win.title(" User Login")

    def add_frame(self):

        self.frame=Frame(self.win,width=500,height=400)
        self.frame.place(x=60,y=40)
        
        x,y=70,20
        

        self.label=Label(self.frame,text="User Login")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=160,y=y+185)
        
        self.emlabel=Label(self.frame,text=" Email")
        self.emlabel.config(font=('times new roman',15,'bold'))
        self.emlabel.place(x=50,y=y+230)
        
        self.email=Entry(self.frame)
        self.email.place(x=200,y=y+230)
        
        self.pslabel=Label(self.frame,text=" Password")
        self.pslabel.config(font=('times new roman',15,'bold'))
        self.pslabel.place(x=50,y=y+260)
        
        self.password=Entry(self.frame,show='*')
        self.password.place(x=200,y=y+260)
        
        self.button=Button(self.frame,text="Sign In",font=('times new roman',15,'bold'),bg='white',fg='black',command=self.users_login)
        self.button.place(x=220,y=y+290)
        
        self.win.mainloop()

    def users_login(self):
        data = (
            self.email.get(),
            self.password.get()
        )
        if self.email.get() == "":
            messagebox.showinfo("Alert !,enter email first")
        elif self.password.get() == "":
            messagebox.showinfo("Alert !,enter password first")
        else:
            res = db.db.student_login(data)
            if res:
                db.db.session = self.email.get()
                messagebox.showinfo("message","login succesfully")
                self.win.destroy()
                r = users.users_navigation.users_navigation()
                r.add_menu()

            else:
                messagebox.showinfo("Alert !","wrong email/password")

    def buttonreg(self):
        messagebox.showinfo("Message","Register Now")
        r=users.users_register.users_register()
        r.add_frame()
        

if __name__ == "__main__":
    x = users_login()
    x.add_frame()
