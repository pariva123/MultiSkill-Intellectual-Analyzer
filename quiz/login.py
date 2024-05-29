from tkinter import *
from tkinter import messagebox
import db.db
import navigation
class login:
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
        self.win.resizable(width=False,height=False)
        self.win.title("  Login Window")
        
    def add_frame(self):
        
        self.frame=Frame(self.win,width=500,height=400)
        self.frame.place(x=60,y=40)
        
        x,y=70,20
        
        self.image=PhotoImage(file='images/login.png')
        self.label=Label(self.frame,image=self.image)
        self.label.place(x=x+80,y=y+0)
        
        self.label=Label(self.frame,text="User Login")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=160,y=y+185)
        
        self.emlabel=Label(self.frame,text="Enter Email")
        self.emlabel.config(font=('times new roman',18,'bold'))
        self.emlabel.place(x=50,y=y+230)
        
        self.email=Entry(self.frame,font=('times new roman',15,'bold'),fg='dark red')
        self.email.place(x=230,y=y+230)
        
        self.pslabel=Label(self.frame,text="Enter Password")
        self.pslabel.config(font=('times new roman',18,'bold'))
        self.pslabel.place(x=50,y=y+270)
        
        self.password=Entry(self.frame,show='*',font=('times new roman',15,'bold'),fg='dark red')
        self.password.place(x=230,y=y+270)
        
        self.button=Button(self.frame,text="Login",font=('times new roman',20,'bold'),bg='white',fg='black',command=self.login)
        self.button.place(x=230,y=y+310)
        
        self.win.mainloop()

    def login(self):
        data = (
            self.email.get(),
            self.password.get()
        )
        if self.email.get() == "":
            messagebox.showinfo("Alert !,enter email first")
        elif self.password.get() == "":
            messagebox.showinfo("Alert !,enter password first")
        else:
            res = db.db.login_page(data)
            if res:
                messagebox.showinfo("message","login succesfully")
                self.win.destroy()
                d=navigation.navigation()
                d.add_menu()
                d.add_frame()
                
            else:
                messagebox.showinfo("Alert !,wrong username/password")


if __name__ == "__main__":
    d = login()
    d.add_frame()
