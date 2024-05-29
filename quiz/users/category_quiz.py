from tkinter import *
from tkinter import messagebox

class category_quiz:
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
        self.win.title(" User Login")

    def add_frame(self):

        self.frame=Frame(self.win,width=500,height=400)
        self.frame.place(x=60,y=40)
        
        x,y=70,20
        
        
        self.label=Label(self.frame,text="Question")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=160,y=y+50)
        
        self.op1label=Label(self.frame,text=" Option 1")
        self.op1label.config(font=('times new roman',15,'bold'))
        self.op1label.place(x=50,y=y+90)
        
        self.option1=Entry(self.frame)
        self.option1.place(x=200,y=y+90)
        
        self.op2label=Label(self.frame,text=" Option 2")
        self.op2label.config(font=('times new roman',15,'bold'))
        self.op2label.place(x=50,y=y+120)
        
        self.option2=Entry(self.frame)
        self.option2.place(x=200,y=y+120)

        self.op3label=Label(self.frame,text=" Option 3")
        self.op3label.config(font=('times new roman',15,'bold'))
        self.op3label.place(x=50,y=y+150)
        
        self.option3=Entry(self.frame)
        self.option3.place(x=200,y=y+150)

        self.op4label=Label(self.frame,text=" Option 4")
        self.op4label.config(font=('times new roman',15,'bold'))
        self.op4label.place(x=50,y=y+180)
        
        self.option4=Entry(self.frame)
        self.option4.place(x=200,y=y+180)
        
        
        
        self.win.mainloop()

  
       
        

    
        

if __name__ == "__main__":
    x=category_quiz()
    x.add_frame()
