from tkinter import *
from tkinter import messagebox
import add_category
import manage_category
import add_question
import manage_question
import edit_question
import manage_users
import edit_users
import scores
import change_password
import add_register
import login


class navigation:
    def __init__(self):

        self.win=Tk()
        self.canvas=Canvas(self.win,width=600,height=720,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width / 2 - 870 / 2)
        y=int(height / 2 -720 / 2)
        
        str1 = "870x720+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)

        self.win.title("Navigation")
    
    
    def add_menu(self):

        self.mainmenu=Menu(self.win)
        self.win.config(menu=self.mainmenu)
        
        self.categorymenu=Menu(self.mainmenu)
        
        self.mainmenu.add_cascade(label="Category",menu=self.categorymenu)
        self.categorymenu.add_command(label="Add Category",command=self.add_category)
        self.categorymenu.add_command(label="Manage Category",command=self.manage_category)
        
        self.questionmenu=Menu(self.mainmenu)
        
        self.mainmenu.add_cascade(label="Question",menu=self.questionmenu)
        self.questionmenu.add_command(label="Add Question",command=self.add_question)
        self.questionmenu.add_command(label="Manage Question",command=self.manage_question)

        self.usersmenu=Menu(self.mainmenu)
        
        self.mainmenu.add_cascade(label="Users",menu=self.usersmenu)
        self.usersmenu.add_command(label="Add Users",command=self.add_users)
        self.usersmenu.add_command(label="Manage Users",command=self.manage_users)
        self.usersmenu.add_command(label="Scores",command=self.scores)

        self.profilemenu=Menu(self.mainmenu)
        
        self.mainmenu.add_cascade(label="Profile",menu=self.profilemenu)
        self.profilemenu.add_command(label="Account",command=self.change_password)
        self.profilemenu.add_command(label="Logout",command=self.logout)
        self.profilemenu.add_separator()
        self.profilemenu.add_command(label="exit",command=self.win.quit)

    def add_frame(self):

        self.image = PhotoImage(file='images/quiztime.png')
        self.label = Label(self.win, image=self.image)
        self.label.place(x=0, y=0)
        self.win.mainloop()
        
    def add_category(self):
        f1 = add_category.add_category()
        f1.add_frame()

    def manage_category(self):
        f2 = manage_category.manage_category()
        f2.add_frame()


    def add_question(self):
        f3 = add_question.add_question()
        f3.add_frame()

    def manage_question(self):
        f3 = manage_question.manage_question()
        f3.add_frame()

    def edit_question(self):
        f4 = edit_question.edit_question()
        f4.add_frame()

    def add_users(self):
        x = add_register.users_register()
        x.add_frame()

    def manage_users(self):
        f5 = manage_users.manage_users()
        f5.add_frame()

    def edit_users(self):
        f6 = edit_users.edit_users()
        f6.add_frame()

    def scores(self):
        f7 = scores.scores()
        f7.add_frame()

    def change_password(self):
        f8=change_password.change_password()
        f8.add_frame()

    def logout(self):
        self.win.destroy()
        x = login.login()
        x.add_frame()
        

if __name__ == "__main__":
    x=navigation()
    x.add_menu()
    x.add_frame()
       

