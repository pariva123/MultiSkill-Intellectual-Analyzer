from tkinter import *
from tkinter import messagebox
import manage_question
import db.db

class edit_question:
    def __init__(self,data=''):
        self.win=Tk()
        self.canvas=Canvas(self.win,width=800,height=400,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-400/2)
        
        str1 = "600x480+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Edit Question")
        
    def add_frame(self):
        
        self.frame=Frame(self.win,width=470,height=400)
        self.frame.place(x=60,y=40)
        
        x,y=70,20

        print(db.db.manage_category())
        OPTIONS = []
        for i in db.db.manage_category():
            OPTIONS.append(i[1])

        self.variable = StringVar(self.win)
        self.variable.set(OPTIONS[0])
    
        self.label=Label(self.frame,text="Edit Question")
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=160,y=y+30)

        self.label1=Label(self.frame,text="Category")
        self.label1.config(font=('times new roman',15,'bold'))
        self.label1.place(x=50,y=y+90)

        self.category = OptionMenu(self.frame, self.variable, *OPTIONS)
        self.category.place(x=200, y=y + 85)
        
        self.qulabel=Label(self.frame,text="Question")
        self.qulabel.config(font=('times new roman',15,'bold'))
        self.qulabel.place(x=50,y=y+120)
        self.question=Entry(self.frame)
        self.question.place(x=200,y=y+120)
        
        self.oplabel=Label(self.frame,text="Option 1")
        self.oplabel.config(font=('times new roman',15,'bold'))
        self.oplabel.place(x=50,y=y+150)
        self.option=Entry(self.frame)
        self.option.place(x=200,y=y+150)
        
        self.op2label=Label(self.frame,text="Option 2")
        self.op2label.config(font=('times new roman',15,'bold'))
        self.op2label.place(x=50,y=y+180)
        self.option2=Entry(self.frame)
        self.option2.place(x=200,y=y+180)
        
        self.op3label=Label(self.frame,text="Option 3")
        self.op3label.config(font=('times new roman',15,'bold'))
        self.op3label.place(x=50,y=y+200)
        self.option3=Entry(self.frame)
        self.option3.place(x=200,y=y+200)
        
        self.op4label=Label(self.frame,text="Option 4")
        self.op4label.config(font=('times new roman',15,'bold'))
        self.op4label.place(x=50,y=y+230)
        self.option4=Entry(self.frame)
        self.option4.place(x=200,y=y+230)

        OPTIONS = [
            'OPTION 1',
            'OPTION 2',
            'OPTION 3',
            'OPTION 4'
        ]

        self.variable1 = StringVar(self.win)
        self.variable1.set(OPTIONS[0])
        self.answer = OptionMenu(self.frame, self.variable1, *OPTIONS, command=self.dropdown)

        self.answer.place(x=200, y=y + 260)

        self.label2=Label(self.frame,text="Answer")
        self.label2.config(font=('times new roman',15,'bold'))
        self.label2.place(x=50,y=y+260)

        if self.data == '':
            self.button=Button(self.frame,text="Submit",font=('times new roman',15,'bold'),bg='white',fg='black',command=self.buttonreg)
            self.button.place(x=220,y=y+310)
        else:
            up =dict(self.data).get('values')
            self.category.insert(0, up[0]),
            self.question.insert(0, up[1]),
            self.option.insert(0, up[2]),
            self.option2.insert(0, up[3]),
            self.option3.insert(0, up[4]),
            self.option4.insert(0, up[5]),
            self.variable1.insert(0, up[6])

            self.button=Button(self.frame, text="Update", font=('times new roman', 15, 'bold'), bg='white',fg='black', command=self.edit_question)
            self.button.place(x=220, y=y + 310)



        self.win.mainloop()

    def buttonreg(self):
        data = (
                self.category.get(),
                self.question.get(),
                self.option.get(),
                self.option2.get(),
                self.option3.get(),
                self.option4.get(),
                self.variable1.get()

            )

        if self.category.get() == "":
            messagebox.showinfo("Alert !","enter category first")
        elif self.question.get() == "":
            messagebox.showinfo("Alert !","enter question first")
        elif self.option.get() == "":
            messagebox.showinfo("Alert !","enter option 1 first")
        elif self.option2.get() == "":
            messagebox.showinfo("Alert !","enter option 2 first")
        elif self.option3.get() == "":
            messagebox.showinfo("Alert !","enter option 3 first")
        elif self.option4.get() == "":
            messagebox.showinfo("Alert !","enter option 4 first")
        elif self.variable1.get() == "":
            messagebox.showinfo("Alert !","enter answer first")
        else:
            res = db.db.add_question(data)
            if res:
                messagebox.showinfo("message", "update succesfully")

            else:
                messagebox.showinfo("Alert !,something went wrong")

    def edit_question(self):
        tup = (
            self.category.get(),
            self.question.get(),
            self.option.get(),
            self.option2.get(),
            self.option3.get(),
            self.option4.get(),
            self.variable1.get(),
            dict(self.data).get('text')
        )
        res = db.db.edit_question(tup)
        if res:
            messagebox.showinfo("message", "data updated successfully")
            self.win.destroy()
            x = manage_question.manage_question()
            x.add_frame()

    def sel(self):
        print(self.var.get())


    def dropdown(self, value, *args):
        print(self.variable1.get())



if __name__=="__main__":
    x=edit_question()
    x.add_frame()
