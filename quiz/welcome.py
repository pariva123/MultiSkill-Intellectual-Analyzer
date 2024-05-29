from tkinter import *
import login


class welcome:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=900,height=600,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width / 2 - 600 / 2)
        y=int(height / 2 -400 / 2)
        
        str1 = "600x500+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("WELCOME TO MULTISKILL INTELLECTUAL ANALYZER")
        
    def add_frame(self):
        self.frame=Frame(self.win,width=470,height=400)
        self.frame.place(x=70,y=40)
        x, y = 70, 20
        
        self.image =PhotoImage(file='images/quiz1.png')
        self.label=Label(self.frame,image=self.image)
        self.label.place(x=x+40,y=y+0)
        self.title=Label(self.frame,text="Welcome to Contest Show")
        self.title.config(font=('times new roman',20,'bold'),fg='maroon')
        self.title.place(x=90,y=250)
        self.button=Button(self.frame,text="Continue",font=('times new roman',20,'bold'),bg='white',fg='black',command=self.login)
        self.button.place(x=x+90,y=y+290)
        
        self.win.mainloop()

    def login(self):
        self.win.destroy()
        d=login.login()
        d.add_frame()


if __name__ == "__main__":
    d = welcome()
    d.add_frame()

