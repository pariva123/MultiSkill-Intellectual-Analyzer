from tkinter import *
from tkinter import messagebox
import users.play_quiz
import users.users_scores
import db.db
import users.users_login



class users_navigation:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=800,height=400,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width / 2 - 600 / 2)
        y=int(height / 2 -400 / 2)
        
        str1 = "600x480+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)

        self.win.title(" Users Navigation")
    
    
    def add_menu(self):
        self.frame=Frame(self.win,width=470,height=400,bg='dark red')
        
        self.lab = Label(self.frame,text="Category",font=('',20),bg="dark red")
        self.lab.place(x=50,y=120)

        self.cat = StringVar(self.frame)

        data = db.db.fetch_category()
        gh = []
        for i in data:
            gh.append(i[1])

        
        self.opt = OptionMenu(self.frame,self.cat,*tuple(gh))
        self.opt.config(fg="dark red",font=('',10))
        self.opt.place(x=200,y=120)
        self.opt.config(width=20)

        self.btn = Button(self.frame,text="Play Quiz",fg="dark red",font=('',15),command=self.play_quiz)
        self.btn.place(x=160,y=170)
        self.frame.place(x=70,y=40)
        x,y=70,40

        self.mainmenu=Menu(self.win)
        self.win.config(menu=self.mainmenu)
        
        self.quizmenu=Menu(self.mainmenu)
        
        self.mainmenu.add_cascade(label="Quiz",menu=self.quizmenu)

        self.quizmenu.add_command(label="Rank",command=self.users_scores)
        self.quizmenu.add_separator()
        self.quizmenu.add_command(label="exit",command=self.win.quit)
        
        self.accountmenu=Menu(self.mainmenu)
        
        self.mainmenu.add_cascade(label="Account",menu=self.accountmenu)
        # self.accountmenu.add_command(label="Profile")
        self.accountmenu.add_command(label="Logout",command=self.logout)
        self.accountmenu.add_separator()
        self.accountmenu.add_command(label="exit",command=self.win.quit)

        self.win.mainloop()


    def play_quiz(self):
        if self.cat.get()!="":
            db.db.category=self.cat.get()

            if len(db.db.fetch_questions(self))==0:
                messagebox.showinfo("Error","Test is not Ready")
            else:
                f1=users.play_quiz.play_quiz()
                f1.add_frame()

        else:
            messagebox.showinfo("Error","Please Enter the category")

    def users_scores(self):
        f2=users.users_scores.users_scores()
        f2.add_frame()

    def logout(self):
        self.win.destroy()
        x = users.users_login.users_login()
        x.add_frame()


if __name__== "__main__":    
        x=users_navigation()
        x.add_menu()
