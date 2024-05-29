from tkinter import *
from tkinter import messagebox
import db.db
class edit_users:
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
        self.win.title("Edit Users")
        
    def add_frame(self):
        
        self.frame=Frame(self.win,width=500,height=400)
        self.frame.place(x=60,y=40)
        
        x,y=70,20
    
        self.label=Label(self.frame,text="Edit Users")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=160,y=y+150)
        
        self.nmlabel=Label(self.frame,text="email")
        self.nmlabel.config(font=('times new roman',15,'bold'))
        self.nmlabel.place(x=50,y=y+200)
        self.email=Entry(self.frame)
        self.email.place(x=200,y=y+200)



        self.pslabel=Label(self.frame,text=" old Password")
        self.pslabel.config(font=('times new roman',15,'bold'))
        self.pslabel.place(x=50,y=y+270)
        self.oldpassword=Entry(self.frame)
        self.oldpassword.place(x=200,y=y+270)

        self.pslabel1 = Label(self.frame, text=" new Password")
        self.pslabel1.config(font=('times new roman', 15, 'bold'))
        self.pslabel1.place(x=50, y=y + 290)
        self.newpassword = Entry(self.frame)
        self.newpassword.place(x=200, y=y + 290)
        
        
        
        self.button=Button(self.frame,text="Update",font=('times new roman',15,'bold'),bg='white',fg='black',command=self.update)
        self.button.place(x=220,y=y+310)
        self.win.mainloop()
    def update(self):
        data=(
            self.email.get(),
            self.oldpassword.get()

        )
        data1=(

            self.newpassword.get(),
            self.email.get(),
        )
        if self.email.get()=="":
            messagebox.showinfo("alert","enter email first")
        elif self.oldpassword.get()=="":
            messagebox.showinfo("alert","enter old password first")
        elif self.newpassword.get()=="":
            messagebox.showinfo("alert","enter new password")
        else:
            res=db.db.update_password(data,data1)
            if res:
                messagebox.showinfo("message","user updated successfully")
                self.oldpassword.delete(0,'end')
                self.newpassword.delete(1,'end')
            else:
                messagebox.showinfo("alert","WRONG USERNAME PASSWORD")
        

  

if __name__=="__main__":
    x=edit_users()
    x.add_frame()
