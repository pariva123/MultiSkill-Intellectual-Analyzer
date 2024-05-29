from tkinter import *
from tkinter import messagebox
import db.db


class add_question:
    def __init__(self):
        self.win=Toplevel()
        self.canvas=Canvas(self.win,width=800,height=400)
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-930/2)
        y=int(height/2-400/2)
        
        str1 = "930x480+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Add Question")
        
    def add_frame(self):

        print(db.db.manage_category())
        OPTIONS = []
        for i in db.db.manage_category():
            OPTIONS.append(i[1])

        self.variable = StringVar(self.win)
        self.variable.set(OPTIONS[0])

        self.frame=Frame(self.win,width=800,height=450)
        self.frame.place(x=60,y=40)
        
        x,y=70,20

        self.image = PhotoImage(file='images/navi.png')
        self.label = Label(self.win, image=self.image)
        self.label.place(x=x + 350, y=y + 20)
    
        self.label=Label(self.frame,text="Add Question")
        self.label.config(font=('times new roman',25,'bold'),fg='dark red')
        self.label.place(x=50,y=y+0)

        self.label1=Label(self.frame,text=' Category')
        self.label1.config(font=('Category',16,'bold'),fg='purple')
        self.label1.place(x=30,y=y+63)

        self.category=OptionMenu(self.frame, self.variable, *OPTIONS)
        self.category.place(x=200,y=y+60)

        self.qulabel=Label(self.frame,text="Question")
        self.qulabel.config(font=('times new roman',18,'bold'),fg='purple')
        self.qulabel.place(x=35,y=y+100)
        self.question=Entry(self.frame,font=('times new roman',12,'bold'),fg='purple')
        self.question.place(x=200,y=y+103)
        
        self.oplabel=Label(self.frame,text="Option 1")
        self.oplabel.config(font=('times new roman',18,'bold'),fg='purple')
        self.oplabel.place(x=35,y=y+133)
        self.option_1=Entry(self.frame,font=('times new roman',12,'bold'),fg='purple')
        self.option_1.place(x=200,y=y+133)
        
        self.op2label=Label(self.frame,text="Option 2")
        self.op2label.config(font=('times new roman',18,'bold'),fg='purple')
        self.op2label.place(x=35,y=y+170)
        self.option_2=Entry(self.frame,font=('times new roman',12,'bold'),fg='purple')
        self.option_2.place(x=200,y=y+170)
        
        self.op3label=Label(self.frame,text="Option 3")
        self.op3label.config(font=('times new roman',18,'bold'),fg='purple')
        self.op3label.place(x=35,y=y+200)
        self.option_3=Entry(self.frame,font=('times new roman',12,'bold'),fg='purple')
        self.option_3.place(x=200,y=y+200)
        
        self.op4label=Label(self.frame,text="Option 4")
        self.op4label.config(font=('times new roman',18,'bold'),fg='purple')
        self.op4label.place(x=35,y=y+230)
        self.option_4=Entry(self.frame,font=('times new roman',12,'bold'),fg='purple')
        self.option_4.place(x=200,y=y+230)

        OPTIONS=[
             'OPTION 1',
             'OPTION 2',
             'OPTION 3',
             'OPTION 4'
         ]

        self.variable1= StringVar(self.win)
        self.variable1.set(OPTIONS[0])
        self.answer=OptionMenu(self.frame,self.variable1,*OPTIONS,command=self.dropdown)

        self.answer.place(x=200, y=y + 260)

        self.label2=Label(self.frame,text='Answer')
        self.label2.config(font=('Answer',16,'bold'),fg='purple')
        self.label2.place(x=35,y=y+260)

        self.button=Button(self.frame,text="Submit",font=('times new roman',20,'bold'),bg='white',fg='purple',command=self.add_question)
        self.button.place(x=200,y=y+310)
        self.win.mainloop()

    def add_question(self):
        data = (
                self.variable.get(),
                self.question.get(),
                self.option_1.get(),
                self.option_2.get(),
                self.option_3.get(),
                self.option_4.get(),
                self.variable1.get(),
                )
        if self.variable.get() == "":
            messagebox.showwarning("Alert","Select category First")
        elif self.question.get() == "":
            messagebox.showwarning("Alert","enter Question first")
        elif self.option_1.get() == "":
            messagebox.showwarning("Alert","enter Option 1 first")
        elif self.option_2.get() == "":
            messagebox.showwarning("Alert","enter Option 2 first")
        elif self.option_3.get() == "":
              messagebox.showwarning("Alert","enter Option 3 first")
        elif self.option_4.get() == "":
            messagebox.showwarning("Alert","enter Option 4 first")
        elif self.variable1.get() == "":
            messagebox.showwarning("Alert","Select answer first")
        else:
            
            res = db.db.add_question(data)
            if res:
                messagebox.showinfo("message","success")
                self.win.destroy()
            else:
                messagebox.showerror("alert","something went wrong")

    def dropdown(self,value,*args):
        print(self.variable1.get())


if __name__ == "__main__":
    x=add_question()
    x.add_frame()
