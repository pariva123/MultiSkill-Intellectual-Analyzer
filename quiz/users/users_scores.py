from tkinter import *
from tkinter.ttk import Treeview
from tkcalendar import DateEntry
import db.db


class users_scores:
    def __init__(self):
        self.win = Tk()
        self.cat = StringVar(self.win)
        self.canvas = Canvas(self.win, width=1000, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1000 / 2)
        y = int(height / 2 - 400 / 2)

        str1 = "1000x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)
        self.win.title(" Users Scores")

    def add_frame(self):
        self.frame = Frame(self.win, width=900, height=350)
        self.frame.place(x=80, y=20)

        self.lab = Label(self.frame, text="Category", font=('', 13))
        self.lab.place(x=80, y=20)

        data = db.db.fetch_category()
        gh = []
        for i in data:
            gh.append(i[1])

        self.opt = OptionMenu(self.frame, self.cat, *tuple(gh))
        self.opt.config(fg="dark red", font=('', 10))
        self.opt.place(x=150, y=20)
        self.opt.config(width=20)

        self.lab = Label(self.frame, text="Date", font=('', 13))
        self.lab.place(x=390, y=20)

        self.dob = DateEntry(self.frame, font=('Comic Sans MS', 13), bg='darkblue',
                             fg='white', borderwidth=2, command=self.getcategory)
        self.dob.place(x=440, y=20)

        self.dob.bind("<<DateEntrySelected>>", self.getcategory)

        x, y = 70, 20
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'), selectmode="extended")
        self.tr.heading('#0', text='Sr No')
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)
        self.tr.heading('#1', text='Question')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='Option 1')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='Option 2')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='Option 3')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#5', text='Option 4')
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#6', text='Answer')
        self.tr.column('#6', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#7', text='Your Answer')
        self.tr.column('#7', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#8', text='Correct/Incorrect')
        self.tr.column('#8', minwidth=0, width=100, stretch=NO)

        self.tot = Label(self.frame,text="Total Score:",font=('',13),fg="red")
        self.tot.place(x=150,y=305)

        self.myscore = Label(self.frame,text="0",font=('',13))
        self.myscore.place(x=470,y=305)

        j = 0
        for i in db.db.users_scores():
            self.tr.insert('', index=j, text=i[0], value=(i[1], i[2]))
            j += 1
        self.tr.place(x=50, y=y + 50)

        self.win.mainloop()

    def getcategory(self,e):
        print("hello")
        lis = [str(self.dob.get_date()), self.cat.get()]
        dr = db.db.getscores(lis)
        print(dr)
        score=0
        for i in self.tr.get_children():
            self.tr.delete(i)
        k = 1
        for i,j in enumerate(dr):
            cor = "Incorrect"
            if eval(j['result']):
                cor="Correct"
                score+=1

            self.tr.insert('','end',text=k,values=(j["question"],j['option_1'],j['option_2'],j['option_3'],j['option_4'],j['answer'],j["selectedopt"],cor))
            k = k+1

        self.myscore["text"]=score


    def getdate(self):
        pass


if __name__ == '__main__':
    d = users_scores()
    d.add_frame()
