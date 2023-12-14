from tkinter import *
# interface module for TK gui toolkit
import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import sqlite3  # module to interface SQLite database
import tkinter as tk
import tkinter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
#import interface
from tkinter import *
import math as m
import datetime
import sqlite3
from tkcalendar import DateEntry
import tkinter.messagebox as mb
import tkinter
from datetime import *
from sqlite3 import *
import datetime
import webbrowser
import tkinter      #for Linux you must install tkinter and scrot
import numpy as np  #pip install numpy
import cv2 as cv    #pip install opencv-python
import pyautogui
from tkcalendar import DateEntry
import tkinter.messagebox as mb
import tkinter.ttk as ttk
from functools import partial
#import interface
database = 'registration'

win = Tk()
win.geometry("2000x1500")
win.title("Login/SignUp")
win.protocol(False,False)

def insertData(values):
    status = 0
    try:
        conn = sqlite3.connect(database)
        conn.execute(
            "create table if not exists Logindata(name varchar(80) not null,username varchar(80) not null unique,password not null)")
        conn.commit()
        conn.execute("insert into Logindata values(?,?,?)", values)
        conn.commit()
    except IntegrityError:
        return 0
    finally:
        status = conn.total_changes
        conn.close()
        return status


def searchData(values):
    conn = sqlite3.connect(database)
    crsr = conn.cursor()
    crsr.execute("select * from Logindata where username = ? and password = ?", values)
    return crsr.fetchall()


def register():
    win2 = Tk()
    win2.geometry("2000x1500")
    win2.title("Registration")
    win2.configure(bg="#FFB03B")
    Label(win2,text="                                      WELCOME TO REGISTRATION PAGE                                                               ",font=("helvetica",30),pady=10,anchor="center").place(x=0,y=80)
    Label(win2,bg="#FFB03B",text="ENTER NAME : ",font=("helvetica", 17)).place(x=650, y=300)
    Label(win2,bg="#FFB03B",text="ENTER USERNAME : ", font=("helvetica", 17)).place(x=650,y=380)
    Label(win2,bg="#FFB03B",text="ENTER PASSWORD : ", font=("helvetica", 17)).place(x=650,y=469)
    e1 = Entry(win2,font=("helvetica",17))
    e2 = Entry(win2,font=("helvetica",17))
    e3 = Entry(win2, show="*",font=("helvetica",17))
    e1.place(x=960,y=300)
    e2.place(x=960, y=380)
    e3.place(x=960, y=465)

    def temp():
        values = (e1.get(), e2.get(), e3.get())
        status = insertData(values)
        if status > 0:
            tkinter.messagebox.showinfo("Done", " Sucessfully Resgistered ! ")
            win2.destroy()
        else:
            tkinter.messagebox.showwarning("Not Registered ",
                                           " Not Registered Due to : 1.Username Already Exist \n 2.Weak Password ")

    b1 = Button(win2, bg="#FFF0A5",text="REGISTER", command=temp,height=2,width=15).place(x=900,y=550)

Label(win,text="                        WELCOME TO STUDENT PERSONALISED APPLICATION                      ",font=("helvetica",30),pady=10,anchor="center").place(x=0,y=100)
Label(win, bg="#2EAC6D",text="ENTER USERNAME : ",font=("helvetica",17)).place(x=650,y=300)
Label(win, bg="#2EAC6D",text="ENTER PASSWORD : ",font=("helvetica",17)).place(x=650,y=380)
e1 = Entry(win,font=("helvetica",15))
e2 = Entry(win, show="*",font=("helvetica",15))
e1.place(x=960,y=300)
e2.place(x=960,y=380)
def newwindow(button_number):
    def Expenses(button_number):
        import datetime
        import webbrowser
        import tkinter  # for Linux you must install tkinter and scrot
        import numpy as np  # pip install numpy
        import cv2 as cv  # pip install opencv-python
        import pyautogui  # pip install PyAutoGUI

        status = ""

        # Find the time for name
        def find_time():
            x = datetime.datetime.now()
            date_for_name = (x.strftime("%d") + "-" + x.strftime("%m") + "-" + x.strftime("%Y") + "-" + x.strftime(
                "%H") + "-" +
                             x.strftime("%M") + "-" + x.strftime("%S"))
            return date_for_name

        def edit_checks(clicked):
            if clicked == "mp4":
                if interface.mp4_format.get() == False:
                    interface.avi_format.set(True)
                else:
                    interface.avi_format.set(False)
            elif clicked == "avi":
                if interface.avi_format.get() == False:
                    interface.mp4_format.set(True)
                else:
                    interface.mp4_format.set(False)

        def result_format():
            if interface.mp4_format.get() == True:
                return ".mp4"
            else:
                return ".avi"

        def result_format2():
            if result_format() == ".mp4":
                return "MP4V"
            else:
                return "XVID"

        interface.video_format.add_checkbutton(label=".mp4", onvalue=1, offvalue=0, variable=interface.mp4_format,
                                               command=lambda: edit_checks("mp4"))
        interface.video_format.add_checkbutton(label=".avi", onvalue=1, offvalue=0, variable=interface.avi_format,
                                               command=lambda: edit_checks("avi"))

        # Start button command
        def create_vid():
            global out
            screen_size = pyautogui.size()
            fourcc = cv.VideoWriter_fourcc(*result_format2())
            out = cv.VideoWriter("Outputs/FrameRecorder " + find_time() + result_format(), fourcc,
                                 interface.switch.get(),
                                 (screen_size))

        def record():
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            out.write(frame)

        def start_record():
            if status in ("end"):
                create_vid()
            status_playing("playing")

        # Report what's happening
        def status_playing(yeter):
            global status
            status = yeter
            if status == "stopped":
                interface.pause["state"] = "disabled"
                interface.start["state"] = "normal"
                interface.canvas.itemconfig(interface.info, text="Paused. Continue Recording with Play")
            elif status == "playing":
                interface.pause["state"] = "normal"
                interface.end["state"] = "normal"
                interface.start["state"] = "disabled"
                interface.canvas.itemconfig(interface.info, text="Recording...")
            elif status == "end":
                interface.canvas.itemconfig(interface.info,
                                            text="Video Saved At Outputs Folder. Let's Create Another One!")
                interface.pause["state"] = "disabled"
                interface.end["state"] = "disabled"
                interface.start["state"] = "normal"

        interface.start.config(command=lambda: start_record())
        interface.end.config(command=lambda: status_playing("end"))
        interface.pause.config(command=lambda: status_playing("stopped"))

        # interface.root.protocol("WM_DELETE_WINDOW", on_closing)
        interface.running = True
        while interface.running:
            interface.root.update()
            interface.switch.place(x=400, y=176, anchor=tkinter.CENTER)
            interface.start.place(x=318, y=230, width=172, height=58)
            interface.pause.place(x=118, y=230, width=172, height=58)
            interface.end.place(x=518, y=230, width=172, height=58)
            interface.root.config(menu=interface.menubar)
            if status == "playing":
                record()
            elif status == "stopped":
                pass
            elif status == "end":
                out.release()
    def Calculator(button_number):
        import math as m
        root = Tk()
        # GIVING TITLE TO THE APPLICATION AS simple calculator
        root.title("Simple Calculator")
        root.resizable(FALSE,FALSE)
        e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="black", bg="white")
        e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)


        def click(to_print):
            old = e.get()
            e.delete(0, END)
            e.insert(0, old + to_print)
            return

        def sc(event):
            key = event.widget
            text = key['text']
            no = e.get()
            result = ''
            if text == 'deg':
                result = str(m.degrees(float(no)))
            if text == 'sin':
                result = str(m.sin(float(no)))
            if text == 'cos':
                result = str(m.cos(float(no)))
            if text == 'tan':
                result = str(m.tan(float(no)))
            if text == 'lg':
                result = str(m.log10(float(no)))
            if text == 'ln':
                result = str(m.log(float(no)))
            if text == 'Sqrt':
                result = str(m.sqrt(float(no)))
            if text == 'x!':
                result = str(m.factorial(float(no)))
            if text == '1/x':
                result = str(1 / (float(no)))
            if text == 'pi':
                if no == "":
                    result = str(m.pi)
                else:
                    result = str(float(no) * m.pi)
            if text == 'e':
                if no == "":
                    result = str(m.e)
                else:
                    result = str(m.e ** float(no))

            e.delete(0, END)
            e.insert(0, result)

        # This function clears all the contents displayed on the computation window.
        def clear():
            e.delete(0, END)
            return

            # This function clears one character from rare end of the string.

        def bksps():
            current = e.get()
            length = len(current) - 1
            e.delete(length, END)

        # This function is defined to evaluate the results and to prompt on the console.
        def evaluate():
            ans = e.get()
            ans = eval(ans)
            e.delete(0, END)
            e.insert(0, ans)

        # Arrangement of buttons for better visualition and computation.
        lg = Button(root, text="log", padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
        lg.bind("<Button-1>", sc)
        ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
        ln.bind("<Button-1>", sc)
        par1st = Button(root, text="(", padx=29, pady=10, relief=RAISED, bg="Black", fg="White",
                        command=lambda: click("("))
        par2nd = Button(root, text=")", padx=30, pady=10, relief=RAISED, bg="Black", fg="White",
                        command=lambda: click(")"))
        dot = Button(root, text=".", padx=29, pady=10, relief=RAISED, fg="black", bg="white",
                     command=lambda: click("."))

        exp = Button(root, text="^", padx=29, pady=10, relief=RAISED, bg="Black", fg="White",
                     command=lambda: click("**"))

        degb = Button(root, text="deg", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
        degb.bind("<Button-1>", sc)
        sinb = Button(root, text="sin", padx=24, pady=10, relief=RAISED, bg="Black", fg="White", )
        sinb.bind("<Button-1>", sc)
        cosb = Button(root, text="cos", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
        cosb.bind("<Button-1>", sc)
        tanb = Button(root, text="tan", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
        tanb.bind("<Button-1>", sc)

        sqrtm = Button(root, text="Sqrt", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
        sqrtm.bind("<Button-1>", sc)
        ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, bg="black", fg="White", command=lambda: clear())
        bksp = Button(root, text="DEL", padx=24, pady=10, relief=RAISED, bg="black", fg="White",
                      command=lambda: bksps())
        mod = Button(root, text=" % ", padx=24, pady=10, relief=RAISED, bg="Black", fg="White",
                     command=lambda: click("%"))
        div = Button(root, text="/", padx=29, pady=10, relief=RAISED, bg="black", fg="Black",
                     command=lambda: click("/"))

        fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
        fact.bind("<Button-1>", sc)
        seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, fg="black", bg="White",
                       command=lambda: click("7"))
        eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, fg="black", bg="White",
                       command=lambda: click("8"))
        nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, bg="white", fg="black",
                      command=lambda: click("9"))
        mult = Button(root, text="X", padx=29, pady=10, relief=RAISED, bg="black", fg="white",
                      command=lambda: click("*"))

        frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
        frac.bind("<Button-1>", sc)
        four = Button(root, text="4", padx=30, pady=10, relief=RAISED, bg="white", fg="black",
                      command=lambda: click("4"))
        five = Button(root, text="5", padx=29, pady=10, relief=RAISED, bg="white", fg="black",
                      command=lambda: click("5"))
        six = Button(root, text="6", padx=29, pady=10, relief=RAISED, bg="white", fg="black", command=lambda: click("6"))
        minus = Button(root, text="-", padx=29, pady=10, relief=RAISED, bg="black", fg="white",
                       command=lambda: click("-"))

        pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
        pib.bind("<Button-1>", sc)
        one = Button(root, text="1", padx=30, pady=10, relief=RAISED, bg="white", fg="black", command=lambda: click("1"))
        two = Button(root, text="2", padx=29, pady=10, relief=RAISED, bg="white", fg="black", command=lambda: click("2"))
        three = Button(root, text="3", padx=29, pady=10, relief=RAISED, bg="white", fg="black",
                       command=lambda: click("3"))
        plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, fg="white", bg="black",
                      command=lambda: click("+"))

        e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
        e_b.bind("<Button-1>", sc)
        zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, bg="white", fg="black",
                      command=lambda: click("0"))
        equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, bg="white", fg="Black",
                       command=lambda: evaluate())

        bksp.grid(row=1, column=0)
        ln.grid(row=1, column=1)
        par1st.grid(row=1, column=2)
        par2nd.grid(row=1, column=3)
        ac.grid(row=1, column=4)

        lg.grid(row=2, column=0)
        degb.grid(row=2, column=1)
        sinb.grid(row=2, column=2)
        cosb.grid(row=2, column=3)
        tanb.grid(row=2, column=4)

        sqrtm.grid(row=3, column=0)
        e_b.grid(row=3, column=1)
        exp.grid(row=3, column=2)
        mod.grid(row=3, column=3)
        div.grid(row=3, column=4)

        fact.grid(row=4, column=0)
        seven.grid(row=4, column=1)
        eight.grid(row=4, column=2)
        nine.grid(row=4, column=3)
        mult.grid(row=4, column=4)

        frac.grid(row=5, column=0)
        four.grid(row=5, column=1)
        five.grid(row=5, column=2)
        six.grid(row=5, column=3)
        minus.grid(row=5, column=4)

        pib.grid(row=6, column=0)
        one.grid(row=6, column=1)
        two.grid(row=6, column=2)
        three.grid(row=6, column=3)
        plus.grid(row=6, column=4)

        dot.grid(row=7, column=1)
        zero.grid(row=7, column=2)
        equal.grid(row=7, column=3)

        root.mainloop()
    def Notes(button_number):
        import sqlite3 as sql
        from tkinter import messagebox
        try:
            con = sql.connect('pin_your_note.db')
            cur = con.cursor()
            cur.execute('''CREATE TABLE notes_table
                                 (date text, notes_title text, notes text)''')
        except:
            print("Connected to table of database")

        def add_notes():
            today = date_entry.get()
            notes_title = notes_title_entry.get()
            notes = notes_entry.get("1.0", "end-1c")
            if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 1):
                messagebox.showerror(message="ENTER REQUIRED DETAILS")
            else:
                cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" % (today, notes_title, notes))
                messagebox.showinfo(message="Note added")
                con.commit()
        def view_notes():
            date = date_entry.get()
            notes_title = notes_title_entry.get()
            if (len(date) <= 0) & (len(notes_title) <= 0):
                sql_statement = "SELECT * FROM notes_table"
            elif (len(date) <= 0) & (len(notes_title) > 0):
                sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" % notes_title
            elif (len(date) > 0) & (len(notes_title) <= 0):
                sql_statement = "SELECT * FROM notes_table where date ='%s'" % date
            else:
                sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" % (date, notes_title)
            cur.execute(sql_statement)
            row = cur.fetchall()
            if len(row) <= 0:
                messagebox.showerror(message="No note found")
            else:
                for i in row:
                    messagebox.showinfo(message="Date: " + i[0] + "\nTitle: " + i[1] + "\nNotes: " + i[2])
        def delete_notes():
            date = date_entry.get()
            notes_title = notes_title_entry.get()
            choice = messagebox.askquestion(message="Do you want to delete all notes?")
            if choice == 'yes':
                sql_statement = "DELETE FROM notes_table"
            else:
                if (len(date) <= 0) & (len(notes_title) <= 0):
                    messagebox.showerror(message="ENTER REQUIRED DETAILS")
                    return
                else:
                    sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" % (
                    date, notes_title)
            cur.execute(sql_statement)
            messagebox.showinfo(message="Note(s) Deleted")
            con.commit()
        def update_notes():
            today = date_entry.get()
            notes_title = notes_title_entry.get()
            notes = notes_entry.get("1.0", "end-1c")
            if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 1):
                messagebox.showerror(message="ENTER REQUIRED DETAILS")
            else:
                sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" % (
                    notes, today, notes_title)
            cur.execute(sql_statement)
            messagebox.showinfo(message="Note Updated")
            con.commit()
        window = Tk()
        window.geometry("2000x1500")
        window.title("Pin Your Note")
        window.configure(bg="black")
        title_label = Label(window, text="                                                PIN YOUR NOTE                                                                       ",font=("helvetica",33)).place(x=0,y=50)
        date_label = Label(window,bg="black",fg="white", text="DATE:",font=("helvetica",15)).place(x=700, y=150)
        date_entry = Entry(window, width=20)
        date_entry.place(x=900,y=155)
        notes_title_label = Label(window,bg="black",fg="white", text="NOTE TITLE:",font=("helvetica",15)).place(x=700, y=190)
        notes_title_entry = Entry(window, width=30)
        notes_title_entry.place(x=900, y=195)
        notes_label = Label(window,bg="black",fg="white", text="TYPE YOUR NOTE HERE:",font=("helvetica",15)).place(x=700, y=235)
        notes_entry = Text(window, width=100, height=10,font=("helvetica",12))
        notes_entry.place(x=700, y=275)
        button1 = Button(window, text='ADD NOTE', bg='#E7B10A', fg='black', font=("helvetica",15),command=add_notes).place(x=700, y=520)
        button2 = Button(window, text='VIEW NOTE', bg='#E7B10A', fg='black',font=("helvetica",15), command=view_notes).place(x=880, y=520)
        button3 = Button(window, text='DELETE NOTE', bg='#E7B10A', fg='black', font=("helvetica",15),command=delete_notes).place(x=1070,y=520)
        button4 = Button(window, text='UPDATE NOTE', bg='#E7B10A', fg='black', font=("helvetica",15),command=update_notes).place(x=1300,y=520)
        window.mainloop()
        con.close()
    def Riddler(button_number):
        import random
        MAX = 10
        MIN = 1
        class Application(Frame):
            __slots__ = "number", "tries", "question", "ans", "qlabel", "list_done"
            def __init__(self, master):
                Frame.__init__(self, master)
                master.minsize(width=500, height=200)
                self.list_done = []
                self.qlabel = Label(self)
                self.grid()
                self.reset()
            def set_game(self):
                qno = self.number
                self.list_done.append(qno)
                if self.number == 1:
                    self.question = "The word 'cruyrecn is jumbled. Guess the right word."
                    self.ans = "currency"
                elif self.number == 2:
                    self.question = "Forwards I am heavy. Backwards I am not. What am I?"
                    self.ans = "ton"
                elif self.number == 3:
                    self.question = "The more of me there is, the less you see. What am I?"
                    self.ans = "darkness"
                elif self.number == 4:
                    self.question = "What holds water yet is full of holes?"
                    self.ans = "sponge"
                elif self.number == 5:
                    self.question = "I can be cracked, I can be made. I can be told and I can be played"
                    self.ans = "joke"
                elif self.number == 6:
                    self.question = "What loses its head every morning and gets it back every night?"
                    self.ans = "pillow"
                elif self.number == 7:
                    self.question = "When you know me, I am nothing. What you don't know me, I am something. What am I?"
                    self.ans = "riddle"
                elif self.number == 8:
                    self.question = "What is it that you ought to keep after you have given it to someone else?"
                    self.ans = "promise"
                elif self.number == 9:
                    self.question = "What kind of coat can be put on only when wet?"
                    self.ans = "paint"
                else:
                    self.question = "He is known to commit a friendly home invasion one night a year, never taking but always leaving stuff behind."
                    self.ans = "santa claus"
            def create_widgets(self):
                if self.qlabel is not None:
                    self.qlabel.grid_forget()
                self.qlabel = Label(self, text=self.question,font=("helvetica",15))
                self.qlabel.grid(row=3, column=3, columnspan=2, sticky=W)
                Label(self,
                      text="TRY TO GUESS THE ANSWER"
                      ,font=("helvetica",15)).grid(row=4, column=3, sticky=W)
                Label(self,
                      text="ROUNDS DONE : 0",
                      font=("helvetica",15)).grid(row=4, column=5, sticky=W)
                Label(self,
                      text="GUESS"
                      ,font=("helvetica",15)).grid(row=5, column=3, sticky=W)
                self.guess_ent = Entry(self,font=("helvetica",15),bg="#7C96AB")
                self.guess_ent.grid(row=6, column=3, sticky=W)
                Button(self,
                       text="ENTER",
                       command=self.get_guess
                       ,font=("helvetica",10),bg='#E7B10A', fg='black').grid(row=8, column=3,sticky=W)
                Button(self,
                       text="RESET",
                       command=self.reset
                       ,font=("helvetica",10),bg='#E7B10A', fg='black').grid(row=9 ,column=3, sticky=W)

                self.results_txt = Text(self, width=40, height=5, wrap=WORD,bg="#7C96AB")
                self.results_txt.grid(row=5, column=5)
            def get_guess(self):
                try:
                    guess = str(self.guess_ent.get())
                except(ValueError):
                    self.display_message("Invalid entry. Try again.")
                else:
                    self.tries += 1
                    if self.tries == 10:
                        self.display_message("You win!!")
                        self.guess_ent.grid_forget()
                    Label(self,
                          text="ROUNDS DONE : " + str(self.tries)
                          ,font=("helvetica",15)).grid(row=4, column=5,sticky=W)
                    self.check_guess(guess)
            def next_question(self):
                self.number = random.randrange(MIN, MAX + 1)
                while self.number in self.list_done:
                    self.number = random.randrange(MIN, MAX + 1)
                self.set_game()
                self.qlabel.grid_forget()
                self.qlabel = Label(self, text=self.question,font=("helvetica",15))
                self.qlabel.grid(row=0, column=3, columnspan=3, sticky=W)
            def check_guess(self, guess):
                if guess == self.ans:
                    self.next_question()
                    self.display_message("CORRECT ANSWER")
                    return
                else:
                    self.display_message("WRONG ANSWER, GAME OVER!!")
                    self.guess_ent.grid_forget()
                    return
            def display_message(self, message):
                self.results_txt.delete(0.0, END)
                self.results_txt.insert(0.0, message)
            def reset(self):
                self.number = random.randrange(MIN, MAX + 1)
                while self.number in self.list_done:
                    self.number = random.randrange(MIN, MAX + 1)
                self.tries = 0
                self.set_game()
                self.create_widgets()
            def resetgame(self):
                self.display_message("Congrats! You guessed correctly. The number was " + \
                                     str(self.number) + ". And it only took you " + \
                                     str(self.tries) + " tries!" + " Click The Reset Button To Play Again")
        def main():
            root = Tk()
            root.title("Guess The Word")
            root.geometry("2000x1500")
            Label(root,text="                                                 SOLVE THESE RIDDLES                                                    ",font=("helvetica",30),bg='#E7B10A', fg='black').grid(row=2,column=0)
            app = Application(root)
            root.mainloop()
        main()
    def Browser(button_number):

        class Window(QMainWindow):
            def __init__(self):
                super(Window, self).__init__()
                self.setWindowTitle("Webbrowser")
                self.setWindowIcon(QIcon("./icon/browser-icon.png"))
                self.setGeometry(300, 50, 1400, 800)

                try:
                    self.browser = QWebEngineView(self)
                    self.browser.setUrl(QUrl("https://google.com"))
                    self.setCentralWidget(self.browser)
                except (Exception,):
                    pass
        def main():
            app = QApplication(sys.argv)
            app.setApplicationName("Webbrowser")
            app.setApplicationVersion("v1.0")
            window = Window()
            window.show()
            app.exec_()

        if __name__ == "__main__":
            main()
    def Todo(button_number):
        import tkinter as tk
        from tkinter import font
        import tkinter.messagebox
        import pickle
        import os
        parent = tk.Tk()
        parent.geometry('1300x500')
        parent.resizable(0, 0)
        def addTask():
            task = entry.get()
            if task.strip() != "":
                leftTasksList.insert(tk.END, task)
                entry.delete(0, tk.END)
            else:
                tk.messagebox.showwarning(title="Warning!", message="You have to enter a task!")

        def deleteSelectedTask():
            try:
                selectedTask = leftTasksList.curselection()
                leftTasksList.delete(selectedTask)
            except:
                tk.messagebox.showwarning(title="Warning!", message="You have to select a task!")
        def deleteAllTask():
            leftTasksList.delete(0, tk.END)
            taskTitle.delete(0, tk.END)
            entry.delete(0, tk.END)
        def saveList():
            tasks = leftTasksList.get(0, leftTasksList.size())
            title = taskTitle.get()
            if len(title) != 0:
                if len(tasks) != 0:
                    pickle.dump(tasks, open("database/" + title + ".txt", "wb"))
                    rightTasksList.insert(tk.END, title)
                else:
                    tk.messagebox.showwarning(title="Warning!", message="You have to add a task!")
            else:
                tk.messagebox.showwarning(title="Warning!", message="You have to insert the title!")
        def loadSelectedList():
            try:
                title = rightTasksList.get(rightTasksList.curselection())
                tasks = pickle.load(open("database/" + title + ".txt", "rb"))
                leftTasksList.delete(0, tk.END)
                taskTitle.delete(0, tk.END)
                taskTitle.insert(tk.END, title)

                for task in tasks:
                    leftTasksList.insert(tk.END, task)
            except:
                tk.messagebox.showwarning(title="Warning!", message="You have to select a Task!")
        def loadFromDatabase():
            lists = os.listdir("database")
            rightTasksList.delete(0, tk.END)
            if len(lists) > 0:
                for item in lists:
                    rightTasksList.insert(tk.END, os.path.splitext(item)[0])  # Remove file extension
            else:
                tk.messagebox.showwarning(title="Warning!", message="You haven't saved anything yet!")

        def deleteSelectedList():
            try:
                selectedTask = rightTasksList.curselection()
                title = rightTasksList.get(selectedTask)
                os.remove("database/" + title + ".txt")
                rightTasksList.delete(selectedTask)
            except:
                tk.messagebox.showwarning(title="Warning!", message="You have to select a list!")
        appTitle = parent.title("To Do List")
        rightContainer = tk.Frame(parent)
        rightContainer.pack(side=tk.RIGHT)
        rightLabel = tk.Label(rightContainer, text="SAVED TASKS", font=("Helvetica", 9, "bold"),
                              #background="#494949",
                              foreground="#494949")
        rightLabel.pack()

        rightScrollbar = tk.Scrollbar(rightContainer)
        rightScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        rightTasksList = tk.Listbox(rightContainer, height=15, width=75, foreground="#494949", background="#fffdf6",
                                    font=("Helvetica", 9))
        rightTasksList.pack()

        rightTasksList.config(yscrollcommand=rightScrollbar.set)
        rightScrollbar.config(command=rightTasksList.yview)

        loadSelectedList = tk.Button(rightContainer, text="Load Task", width=74, command=loadSelectedList,
                                     background="#faf6e9", foreground="#494949", font=("Helvetica", 9))
        loadSelectedList.pack()

        loadFromDatabase = tk.Button(rightContainer, text="Load Tasks From Database", width=74,
                                     command=loadFromDatabase,
                                     background="#faf6e9", foreground="#494949", font=("Helvetica", 9))
        loadFromDatabase.pack()
        deleteSelectedList = tk.Button(rightContainer, text="Delete Task", width=74, command=deleteSelectedList,
                                       background="#faf6e9", foreground="#494949", font=("Helvetica", 9))
        deleteSelectedList.pack()

        leftContainer = tk.Frame(parent)
        leftContainer.pack(side=tk.LEFT)
        enterTitle = tk.Label(leftContainer, text="TASK TITLE: ", width=15, height=1, font=("Helvetica", 9, "bold"),
                              foreground="#494949")
        enterTitle.pack()

        taskTitle = tk.Entry(leftContainer, width=30, background="#fffdf6", foreground="#494949",
                             font=("Helvetica", 9))
        taskTitle.pack()
        leftScrollbar = tk.Scrollbar(leftContainer)
        leftScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        leftTasksList = tk.Listbox(leftContainer, height=11, width=80, foreground="#494949", background="#fffdf6",
                                   font=("Helvetica", 9))
        leftTasksList.pack()

        leftTasksList.config(yscrollcommand=leftScrollbar.set)
        leftScrollbar.config(command=leftTasksList.yview)
        entry = tk.Entry(leftContainer, width=80, background="#494949", foreground="#fffdf6", font=("helvetica", 9))
        entry.pack()
        addBtn = tk.Button(leftContainer, text="Add Task", width=68, command=addTask, background="#faf6e9",
                           foreground="#494949", font=("Helvetica", 9))
        addBtn.pack()

        deleteBtn = tk.Button(leftContainer, text="Delete Task", width=68, command=deleteSelectedTask,
                              background="#faf6e9",
                              foreground="#494949", font=("Helvetica", 9))
        deleteBtn.pack()
        deleteAllBtn = tk.Button(leftContainer, text="Delete All", width=68, command=deleteAllTask,
                                 background="#faf6e9",
                                 foreground="#494949", font=("Helvetica", 9))
        deleteAllBtn.pack()

        saveBtn = tk.Button(leftContainer, text="Save List", width=68, command=saveList, background="#faf6e9",
                            foreground="#494949", font=("Helvetica", 9))
        saveBtn.pack()
        parent.mainloop()
    root = tk.Tk()
    root.title("Student Personalized App")
    root.geometry("2000x1500")
    label = tk.Label(root,bg="#BDCDD6",text="                                                STUDENT PERSONALISED APPLICATION                                                 ")
    root.config(bg="#4C0033")
    label.config(font=("Arial", 30), pady=10)
    label.grid(row=0, column=0, columnspan=3)
    button1 = tk.Button(root,bg="#BDCDD6",text="TO-DO LIST", width="30", height="5",font=("helvetica",12), command=lambda: Todo(1))
    button2 = tk.Button(root,bg="#BDCDD6" ,text="BROWSER", width="30", height="5", font=("helvetica",12),command=lambda: Browser(2))
    button3 = tk.Button(root, text="NOTES", width="30", height="5",font=("helvetica",12),bg="#BDCDD6", command=lambda: Notes(3))
    button4 = tk.Button(root, text="RIDDLER", width="30", height="5",font=("helvetica",12),bg="#BDCDD6", command=lambda: Riddler(4))
    button5 = tk.Button(root, text="CALCULATOR", width="30", height="5",font=("helvetica",12) ,bg="#BDCDD6",command=lambda: Calculator(5))
    button6 = tk.Button(root,bg="#BDCDD6", text="ACTIVITY RECORDER", width="30", height="5",font=("helvetica",12) ,command=lambda: Expenses(6))
    button1.grid(row=1, column=0, padx=10, pady=10)
    button2.grid(row=1, column=1, padx=10, pady=10)
    button3.grid(row=1, column=2, padx=10, pady=10)
    button4.grid(row=2, column=0, padx=10, pady=10)
    button5.grid(row=2, column=1, padx=10, pady=10)
    button6.grid(row=2, column=2, padx=10, pady=10)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.mainloop()
def temp():
    values = (e1.get(), e2.get())
    usr = searchData(values)
    if not usr:
        tkinter.messagebox.showwarning("Not Login", "Invalid Credentials")
    else:
        win3 = Tk()
        win3.geometry("2000x1500")
        win.destroy()
        win3.title("Welcome")
        win3.configure(bg="#9CFF2E")
        Label(win3, text="                                                 WELCOME : " + usr[0][0].upper()+"                                                                                        ", font=("helvetica", 30)).place(x=0, y=80)
        Button(win3, bg="#A8E890",text="ENTER INTO YOUR APPLICATION", command=lambda: newwindow(1), font=("helvetica", 25)).place(
            x=650, y=300)
b2 = Button(win,bg="#9EE6CF",text="Login", command=temp,height=2,width=20).place(x=970,y=450)
b3 = Button(win, bg="#9EE6CF",text="New User! Sign Up ", command=register,height=2,width=25).place(x=720,y=450)
win.configure(bg="#2EAC6D")
win.mainloop()