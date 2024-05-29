from tkinter import *
class login:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=600,height=400,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-400/2)
        
        str1 = "600x500+" +str(x) +"+" +str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Login Window")
        
    def add_frame(self):
        self.frame=Frame(self.win,width=400,height=500)
        self.frame.place(x=80,y=50)
        
        x,y=70,20
        
        self.image=PhotoImage(file='image/login.png')
        self.label=Label(self.frame,image=self.image)
        self.label.place(x=x+80,y=y+0)
        
        self.label=Label(self.frame,text="User Login")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=140,y=y+150)
        
        self.emlabel=Label(self.frame,text="Enter Email")
        self.emlabel.place(x=50,y=y+230)
        self.email=Entry(self.frame,font='bold')

        self.pslabel=Label(self.frame,text="Enter Email")
        self.pslabel.config(font=('times new roman',20,'bold'))
        self.pslabel.place(x=50,y=y+260)
        self.password=Entry(self.frame,font='bold')
        self.pslabel.place(x=200,y=y+260)
        
        self.button=Button(self.frame,text="Login")
        self.button.place(x=50,y=200,font=('times new roman',20,'bold'))
        
        self.win.mainloop()

        
if __name__=="__main__":
        d = login()
        d.add_frame()
