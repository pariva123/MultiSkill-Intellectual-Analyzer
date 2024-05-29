from tkinter import *
from tkinter import messagebox
import db.db
class change_password:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=900,height=600,bg='rosy brown')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-500/2)
        
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Change Password")
        
    def add_frame(self):
        
        self.frame=Frame(self.win,width=500,height=400,bg='rosy brown')
        self.frame.place(x=60,y=40)

        x, y = 70, 20

        # self.img=PhotoImage(file="images/up.png")
        # self.label=Label(self.frame,image=self.img)
        # self.label.place(x=x+330,y=y+250)

        self.eml = Label(self.frame, text="Email: ")
        self.eml.config(font=("Verdana", 18), fg='black')
        self.eml.place(x=20, y=y + 150)

        self.email = Entry(self.frame, font='verdana 15', fg='blue')
        self.email.place(x=240, y=y + 150)

        self.labelopass = Label(self.frame, text="Old Password: ")
        self.labelopass.config(font=("Verdana", 18), fg='black')
        self.labelopass.place(x=20, y=y + 220)

        self.oldpass = Entry(self.frame, font='verdana 15',fg='blue')
        self.oldpass.place(x=240, y=y + 220)

        self.labelnpass = Label(self.frame, text="New Password: ")
        self.labelnpass.config(font=("Verdana", 18), fg='black')
        self.labelnpass.place(x=20, y=y + 290)

        self.newpass = Entry(self.frame, font='verdana 15',fg='blue')
        self.newpass.place(x=240, y=y + 290)

        self.button = Button(self.frame, text="SUBMIT", bg='white', fg='black', font=('Verdana', 18),
                             command=self.update_password)
        self.button.place(x=240, y=y + 340)

        self.win.mainloop()

    def update_password(self):

        password = (
            self.email.get(),
            self.oldpass.get()
        )
        password1=(
            self.newpass.get(),
            self.email.get()

        )
        res=db.db.update_admin_pass(password,password1)
        if res:
            messagebox.showinfo("Message", 'Password Updated Successfully')
            self.win.destroy()
        else:
            messagebox.showinfo("Alert!", 'Please try again')
        

if __name__ == "__main__":
    x=change_password()
    x.add_frame()
