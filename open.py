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