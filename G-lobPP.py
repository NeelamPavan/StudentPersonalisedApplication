import tkinter as tk
import tkinter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
from tkinter import *
import math as m
import datetime
import sqlite3
from tkcalendar import DateEntry
import tkinter.messagebox as mb
import tkinter
from datetime import *
from sqlite3 import *
from tkcalendar import DateEntry
import tkinter.messagebox as mb
import tkinter.ttk as ttk
from functools import partial
def Expenses(button_number):
        import math as m
        root = Tk()
        # GIVING TITLE TO THE APPLICATION AS simple calculator
        root.title("Simple Calculator")
        e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
        e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

        # Creating some userdefined functions for the operations involved in the application.
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
        dot = Button(root, text=".", padx=29, pady=10, relief=RAISED, bg="Green", fg="Black",
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
        ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, bg="Dark Red", fg="White", command=lambda: clear())
        bksp = Button(root, text="DEL", padx=24, pady=10, relief=RAISED, bg="Dark Red", fg="White",
                      command=lambda: bksps())
        mod = Button(root, text=" % ", padx=24, pady=10, relief=RAISED, bg="Black", fg="White",
                     command=lambda: click("%"))
        div = Button(root, text="/", padx=29, pady=10, relief=RAISED, bg="yellow", fg="Black",
                     command=lambda: click("/"))

        fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
        fact.bind("<Button-1>", sc)
        seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White",
                       command=lambda: click("7"))
        eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",
                       command=lambda: click("8"))
        nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",
                      command=lambda: click("9"))
        mult = Button(root, text="X", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black",
                      command=lambda: click("*"))

        frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
        frac.bind("<Button-1>", sc)
        four = Button(root, text="4", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White",
                      command=lambda: click("4"))
        five = Button(root, text="5", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",
                      command=lambda: click("5"))
        six = Button(root, text="6", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
        minus = Button(root, text="-", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black",
                       command=lambda: click("-"))

        pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
        pib.bind("<Button-1>", sc)
        one = Button(root, text="1", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
        two = Button(root, text="2", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
        three = Button(root, text="3", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",
                       command=lambda: click("3"))
        plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black",
                      command=lambda: click("+"))

        e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
        e_b.bind("<Button-1>", sc)
        zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",
                      command=lambda: click("0"))
        equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, bg="Dark Orange", fg="Black",
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

        # In[ ]:

def Calculator(button_number):
    import math as m
    root = Tk()
    # GIVING TITLE TO THE APPLICATION AS simple calculator
    root.title("Simple Calculator")
    e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
    e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

    # Creating some userdefined functions for the operations involved in the application.
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
    par1st = Button(root, text="(", padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("("))
    par2nd = Button(root, text=")", padx=30, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click(")"))
    dot = Button(root, text=".", padx=29, pady=10, relief=RAISED, bg="Green", fg="Black", command=lambda: click("."))

    exp = Button(root, text="^", padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("**"))

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
    ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, bg="Dark Red", fg="White", command=lambda: clear())
    bksp = Button(root, text="DEL", padx=24, pady=10, relief=RAISED, bg="Dark Red", fg="White", command=lambda: bksps())
    mod = Button(root, text=" % ", padx=24, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("%"))
    div = Button(root, text="/", padx=29, pady=10, relief=RAISED, bg="yellow", fg="Black", command=lambda: click("/"))

    fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
    fact.bind("<Button-1>", sc)
    seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
    eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
    nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))
    mult = Button(root, text="X", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black", command=lambda: click("*"))

    frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
    frac.bind("<Button-1>", sc)
    four = Button(root, text="4", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
    five = Button(root, text="5", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
    six = Button(root, text="6", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
    minus = Button(root, text="-", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black", command=lambda: click("-"))

    pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
    pib.bind("<Button-1>", sc)
    one = Button(root, text="1", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
    two = Button(root, text="2", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
    three = Button(root, text="3", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
    plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black", command=lambda: click("+"))

    e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
    e_b.bind("<Button-1>", sc)
    zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))
    equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, bg="Dark Orange", fg="Black",
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

    # In[ ]:
def Notes(button_number):
    import sqlite3 as sql
   # from tkinter import *
    from tkinter import messagebox

    # Create database connection and connect to table
    try:
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE notes_table
                             (date text, notes_title text, notes text)''')
    except:
        print("Connected to table of database")

    # Insert a row of data
    def add_notes():
        # Get input values
        today = date_entry.get()
        notes_title = notes_title_entry.get()
        notes = notes_entry.get("1.0", "end-1c")
        # Raise a prompt for missing values
        if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 1):
            messagebox.showerror(message="ENTER REQUIRED DETAILS")
        else:
            # Insert into the table
            cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" % (today, notes_title, notes))
            messagebox.showinfo(message="Note added")
            # Commit to preserve the changes
            con.commit()

    # Display all the notes
    def view_notes():
        # Obtain all the user input
        date = date_entry.get()
        notes_title = notes_title_entry.get()
        # If no input is given, retrieve all notes
        if (len(date) <= 0) & (len(notes_title) <= 0):
            sql_statement = "SELECT * FROM notes_table"

        # Retrieve notes matching a title
        elif (len(date) <= 0) & (len(notes_title) > 0):
            sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" % notes_title
        # Retrieve notes matching a date
        elif (len(date) > 0) & (len(notes_title) <= 0):
            sql_statement = "SELECT * FROM notes_table where date ='%s'" % date
        # Retrieve notes matching the date and title
        else:
            sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" % (date, notes_title)

        # Execute the query
        cur.execute(sql_statement)
        # Obtain all the contents of the query
        row = cur.fetchall()
        # Check if none was retrieved
        if len(row) <= 0:
            messagebox.showerror(message="No note found")
        else:
            # Print the notes
            for i in row:
                messagebox.showinfo(message="Date: " + i[0] + "\nTitle: " + i[1] + "\nNotes: " + i[2])

    # Delete the notes
    def delete_notes():
        # Obtain input values
        date = date_entry.get()
        notes_title = notes_title_entry.get()
        # Ask if user wants to delete all notes
        choice = messagebox.askquestion(message="Do you want to delete all notes?")
        # If yes is selected, delete all
        if choice == 'yes':
            sql_statement = "DELETE FROM notes_table"
        else:
            # Delete notes matching a particular date and title
            if (len(date) <= 0) & (len(notes_title) <= 0):
                # Raise error for no inputs
                messagebox.showerror(message="ENTER REQUIRED DETAILS")
                return
            else:
                sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" % (date, notes_title)
        # Execute the query
        cur.execute(sql_statement)
        messagebox.showinfo(message="Note(s) Deleted")
        con.commit()

    # Update the notes
    def update_notes():
        # Obtain user input
        today = date_entry.get()
        notes_title = notes_title_entry.get()
        notes = notes_entry.get("1.0", "end-1c")
        # Check if input is given by the user
        if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 1):
            messagebox.showerror(message="ENTER REQUIRED DETAILS")
        # update the note
        else:
            sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" % (
            notes, today, notes_title)

        cur.execute(sql_statement)
        messagebox.showinfo(message="Note Updated")
        con.commit()

    # Invoke call to class to view a window
    window = Tk()
    # Set dimensions of window and title
    window.geometry("500x300")
    window.title("Pin Your Note")

    title_label = Label(window, text="Pin Your Note").pack()
    # Read inputs
    # Date input
    date_label = Label(window, text="Date:").place(x=10, y=20)
    date_entry = Entry(window, width=20)
    date_entry.place(x=50, y=20)
    # Notes Title input
    notes_title_label = Label(window, text="Notes title:").place(x=10, y=50)
    notes_title_entry = Entry(window, width=30)
    notes_title_entry.place(x=80, y=50)
    # Notes input
    notes_label = Label(window, text="Notes:").place(x=10, y=90)
    notes_entry = Text(window, width=50, height=5)
    notes_entry.place(x=60, y=90)

    # Perform notes functions
    button1 = Button(window, text='Add Notes', bg='Turquoise', fg='Red', command=add_notes).place(x=10, y=190)
    button2 = Button(window, text='View Notes', bg='Turquoise', fg='Red', command=view_notes).place(x=110, y=190)
    button3 = Button(window, text='Delete Notes', bg='Turquoise', fg='Red', command=delete_notes).place(x=210, y=190)
    button4 = Button(window, text='Update Notes', bg='Turquoise', fg='Red', command=update_notes).place(x=320, y=190)

    # close the app
    window.mainloop()
    con.close()
def Riddler(button_number):
    import random

    # (Lower & upper limit)
    MAX = 10
    MIN = 1

    class Application(Frame):
        """The GUI application (Guess My Number)."""

        __slots__ = "number", "tries", "question", "ans", "qlabel", "list_done"

        def __init__(self, master):
            """Initialize Frame."""
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
            """Program all the widgets to be used."""
            if self.qlabel is not None:
                self.qlabel.grid_forget()

            self.qlabel = Label(self, text=self.question)

            self.qlabel.grid(row=0, column=0, columnspan=2, sticky=W)

            # Label(self, text = self.question).grid(row=0, column=0, columnspan=2, sticky=W)

            Label(self,
                  text="Try to guess the answer"
                  ).grid(row=1, column=0, columnspan=2, sticky=W)

            Label(self,
                  text="Rounds done : 0"
                  ).grid(row=0, column=2, columnspan=1, sticky=W)

            Label(self,
                  text="Guess"
                  ).grid(row=2, column=0, sticky=W)

            # Entry widget to allow guessing
            self.guess_ent = Entry(self)
            self.guess_ent.grid(row=2, column=1, sticky=W)

            # Submit button to obtain guess
            Button(self,
                   text="Enter",
                   command=self.get_guess
                   ).grid(row=2, column=2, columnspan=4, sticky=W)
            Button(self,
                   text="Reset",
                   command=self.reset
                   ).grid(row=1, column=2, columnspan=1, sticky=W)

            self.results_txt = Text(self, width=40, height=5, wrap=WORD)
            self.results_txt.grid(row=3, column=0, columnspan=3)

        def get_guess(self):
            """Obtain the player's guess and verify it."""
            try:
                guess = str(self.guess_ent.get())
            except(ValueError):
                self.display_message("Invalid entry. Try again.")
            else:
                self.tries += 1
                if self.tries == 10:
                    self.display_message("You win!!")
                    self.guess_ent.grid_forget()
                    # Label(self, text="     You won!!                    ").grid(row=3, column=0, columnspan=3)
                    # print("You won!!")
                    # exit(0)
                Label(self,
                      text="Rounds done : " + str(self.tries)
                      ).grid(row=0, column=2, columnspan=1, sticky=W)
                self.check_guess(guess)

        def next_question(self):

            self.number = random.randrange(MIN, MAX + 1)
            while self.number in self.list_done:
                self.number = random.randrange(MIN, MAX + 1)

            self.set_game()

            # Label(self, text="                                       ").grid(row=0, column=0, columnspan=2, sticky=W)

            self.qlabel.grid_forget()

            self.qlabel = Label(self, text=self.question)

            # Label(self, text=self.question).grid(row=0, column=0, columnspan=2, sticky=W)

            self.qlabel.grid(row=0, column=0, columnspan=2, sticky=W)

            # self.qlabel.text = self.question

        def check_guess(self, guess):
            """
            Verify if the player's guess is correct.
            Keyword argument:
            guess - the int value to be verified
            """

            if guess == self.ans:
                self.next_question()
                self.display_message("Correct Answer")
                return

            else:
                self.display_message("Wrong Answer. Game Over!")
                self.guess_ent.grid_forget()
                # Label(self, text = "     Wrong Answer. Game Over!     ").grid(row=3, column=0, columnspan=3)
                # print("Wrong Answer. Game Over!")
                # exit(0)
                return

            '''if guess < MIN or guess > MAX:
                self.display_message("Invalid Input, Guess Out Side Of Range.")
                self.tries -= 1  # This try doesn't count
                return

            # If guess equals the number, end current game.
            if guess == self.number:
                self.resetgame()
                return

            # Otherwise, see if guess is higher or lower than the chosen number.
            if guess < self.number:
                self.display_message("Guess Higher...")
                return
            elif guess > self.number:
                self.display_message("Guess Lower...")
                return
            '''

        def display_message(self, message):
            """
            Display a message on the text box.
            Keyword argument:
            message -- the message to be displayed

            """
            self.results_txt.delete(0.0, END)
            self.results_txt.insert(0.0, message)

        def reset(self):
            """Prepare for a new game."""
            # Word to be guessed by player.
            self.number = random.randrange(MIN, MAX + 1)
            while self.number in self.list_done:
                self.number = random.randrange(MIN, MAX + 1)

            self.tries = 0

            self.set_game()

            self.create_widgets()
            '''self.number = random.randrange(MIN, MAX + 1)
            self.display_message("Game Reset. Please enter another number to play again.")
            self.tries = 0
            Label(self,
                  text="Number Of Tries: " + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)'''

        def resetgame(self):
            self.display_message("Congrats! You guessed correctly. The number was " + \
                                 str(self.number) + ". And it only took you " + \
                                 str(self.tries) + " tries!" + " Click The Reset Button To Play Again")

    def main():
        """Kickstart Guess My Number."""
        root = Tk()
        root.title("Guess The Word")
        app = Application(root)
        root.mainloop()

    # start Guess The Number
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

    # ==== PARENT (WINDOW) ====
    parent = tk.Tk()
    parent.geometry('1000x345')
    parent.resizable(0, 0)

    # ==== FUNCTIONS ====

    # ==== LEFT CONTAINER ====
    # addTask
    def addTask():
        task = entry.get()
        if task.strip() != "":
            leftTasksList.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning(title="Warning!", message="You have to enter a task!")

    # deleteSelectedTask
    def deleteSelectedTask():
        try:
            selectedTask = leftTasksList.curselection()
            leftTasksList.delete(selectedTask)
        except:
            tk.messagebox.showwarning(title="Warning!", message="You have to select a task!")

    # deleteAllTask
    def deleteAllTask():
        leftTasksList.delete(0, tk.END)
        taskTitle.delete(0, tk.END)
        entry.delete(0, tk.END)

    # saveTask
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

    # ==== RIGHT CONTAINER ====
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
            tk.messagebox.showwarning(title="Warning!", message="You have to select a list!")

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

    # ==== GUI ====

    # Title
    appTitle = parent.title("To Do List")

    # ==== RIGHT CONTAINER ====
    # Container2
    rightContainer = tk.Frame(parent)
    rightContainer.pack(side=tk.RIGHT)

    # Label
    rightLabel = tk.Label(rightContainer, text="Saved Lists", font=("MS Sans Serif", 9, "bold"), background="#494949",
                          foreground="#fffdf6")
    rightLabel.pack()

    # Scrollbar
    rightScrollbar = tk.Scrollbar(rightContainer)
    rightScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ListBox
    rightTasksList = tk.Listbox(rightContainer, height=15, width=75, foreground="#494949", background="#fffdf6",
                                font=("Sans Serif", 9))
    rightTasksList.pack()

    rightTasksList.config(yscrollcommand=rightScrollbar.set)
    rightScrollbar.config(command=rightTasksList.yview)

    # loadSelectedList
    loadSelectedList = tk.Button(rightContainer, text="Load List", width=74, command=loadSelectedList,
                                 background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
    loadSelectedList.pack()

    # loadFromDatabase
    loadFromDatabase = tk.Button(rightContainer, text="Load Lists From Database", width=74, command=loadFromDatabase,
                                 background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
    loadFromDatabase.pack()

    # deleteSelectedList
    deleteSelectedList = tk.Button(rightContainer, text="Delete List", width=74, command=deleteSelectedList,
                                   background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
    deleteSelectedList.pack()

    # ==== LEFT CONTAINER ====
    leftContainer = tk.Frame(parent)
    leftContainer.pack(side=tk.LEFT)

    # taskTitle
    enterTitle = tk.Label(leftContainer, text="List Title: ", width=15, height=1, font=("MS Sans Serif", 9, "bold"),
                          foreground="#494949")
    enterTitle.pack()

    taskTitle = tk.Entry(leftContainer, width=30, background="#fffdf6", foreground="#494949", font=("Sans Serif", 9))
    taskTitle.pack()

    # Scrollbar
    leftScrollbar = tk.Scrollbar(leftContainer)
    leftScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ListBox
    leftTasksList = tk.Listbox(leftContainer, height=11, width=80, foreground="#494949", background="#fffdf6",
                               font=("Sans Serif", 9))
    leftTasksList.pack()

    leftTasksList.config(yscrollcommand=leftScrollbar.set)
    leftScrollbar.config(command=leftTasksList.yview)

    # Entry (input)
    entry = tk.Entry(leftContainer, width=80, background="#494949", foreground="#fffdf6", font=("Sans Serif", 9))
    entry.pack()

    # addBtn
    addBtn = tk.Button(leftContainer, text="Add Task", width=68, command=addTask, background="#faf6e9",
                       foreground="#494949", font=("Sans Serif", 9))
    addBtn.pack()

    # deleteBtn
    deleteBtn = tk.Button(leftContainer, text="Delete Task", width=68, command=deleteSelectedTask, background="#faf6e9",
                          foreground="#494949", font=("Sans Serif", 9))
    deleteBtn.pack()

    # deleteAllBtn
    deleteAllBtn = tk.Button(leftContainer, text="Delete All", width=68, command=deleteAllTask, background="#faf6e9",
                             foreground="#494949", font=("Sans Serif", 9))
    deleteAllBtn.pack()

    # saveBtn
    saveBtn = tk.Button(leftContainer, text="Save List", width=68, command=saveList, background="#faf6e9",
                        foreground="#494949", font=("Sans Serif", 9))
    saveBtn.pack()

    # ==== RUN GUI ====
    parent.mainloop()

root = tk.Tk()
root.title("Student Personalized App")
root.geometry("2000x1500")
label = tk.Label(root, text="Student Personalized Application",bg="#C84B31")
root.config(bg="#C84B31")
label.config(font=("Arial",40), pady=10)
label.grid(row=0, column=0, columnspan=3)
button1 = tk.Button(root, text="TO-DO LIST",width="30",height="5", command=lambda: Todo(1))
button2 = tk.Button(root, text="BROWSER",width="30",height="5", command=lambda: Browser(2))
button3 = tk.Button(root, text="NOTES",width="30",height="5", command=lambda: Notes(3))
button4 = tk.Button(root, text="RIDDLER",width="30",height="5", command=lambda: Riddler(4))
button5 = tk.Button(root, text="CALCULATOR",width="30",height="5", command=lambda: Calculator(5))
button6 = tk.Button(root, text="EXPENSES",width="30",height="5", command=lambda: Expenses(6))
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
