from tkinter import *
import db.db
from tkinter import messagebox
# import category_quiz


class play_quiz:
    def __init__(self):
        self.win=Tk()
        self.score = 0
        self.ques = 0
        self.canvas=Canvas(self.win,width=900,height=600,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-500/2)
        
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False,height=False)
        self.win.title("Play")
        
    def add_frame(self):
        
        self.frame=Frame(self.win, width=500, height=400)
        self.frame.place(x=60,y=40)

        self.questions = db.db.fetch_questions(self)

        x, y = 70, 20
    
        self.label=Label(self.frame,text=str(self.ques+1)+self.questions[self.ques][2])
        self.label.config(font=('times new roman',20,'bold'))
        self.label.place(x=20,y=y+100)

        self.ques_id = self.questions[self.ques][0]
        self.answer = StringVar(self.frame,'$#')

        self.radio = Radiobutton(self.frame,value="OPTION 1",text=self.questions[self.ques][3],variable=self.answer)
        self.radio.place(x=20,y=y+140)

        self.radio = Radiobutton(self.frame,value="OPTION 2", text=self.questions[self.ques][4],variable=self.answer)
        self.radio.place(x=20, y=y + 180)

        self.radio = Radiobutton(self.frame,value="OPTION 3", text=self.questions[self.ques][5],variable=self.answer)
        self.radio.place(x=20, y=y + 220)
        self.radio = Radiobutton(self.frame,value="OPTION 4", text=self.questions[self.ques][6],variable=self.answer)
        self.radio.place(x=20, y=y + 260)

        self.button = Button(self.frame,text="Submit",font=('times new roman',15,'bold'),bg='white',fg='black',command=self.category_quiz)
        self.button.place(x=160,y=y+300)
        self.win.mainloop()

    def category_quiz(self):
        try:

            if (self.answer.get()) != "$#":
                answr = "False"
                print(self.answer.get(),self.questions[self.ques][7])
                if self.answer.get()==self.questions[self.ques][7]:
                    answr="True"
                    self.score = self.score + 1
                tup = [self.ques_id,answr,self.answer.get()]
                db.db.set_question_result(tup)
            else:
                tup = [self.ques_id, "False", ""]
                db.db.set_question_result(tup)

            self.frame.destroy()


            self.ques
            self.ques = self.ques +1
            self.add_frame()
        except:
            tup = [self.questions[0][1],self.score]
            db.db.addtotalscore(tup)
            messagebox.showinfo("Thanks","Your score has been submitted")
            self.win.destroy()

    
    

    

if __name__=="__main__":
    x=play_quiz()
    x.add_frame()
