import backend

from tkinter import *

import tkinter as tk


win = Tk()

win.title("Moody")


date = tk.StringVar()

earn = tk.StringVar()

excerise = tk.StringVar()

study = tk.StringVar()

diet = tk.StringVar()

python = tk.StringVar()


def get_selected_row(event):

    print("yes")
    global selected_row

    index = list.curselection()[0]
    selected_row = list.get(index)
    

    date_entry.delete(0,END)

    date_entry.insert(END,selected_row[1])

    earn_entry.delete(0,END)

    earn_entry.insert(END,selected_row[2])

    excerise_entry.delete(0,END)

    excerise_entry.insert(END,selected_row[3])

    study_entry.delete(0,END)

    study_entry.insert(END,selected_row[4])

    diet_entry.delete(0,END)

    diet_entry.insert(END,selected_row[5])

    python_entry.delete(0,END)

    python_entry.insert(END,selected_row[6])



def delete_command():

    backend.delete(selected_row[0]) 


def add_command():

    backend.insert(date.get(), earn.get(), excerise.get(), study.get(), diet.get(), python.get())

    list.delete(0,END)

    list.insert(END,(date.get(),earn.get(),excerise.get(),study.get(),diet.get(),python.get()))


def view_command():

    list.delete(0, END)

    for row in backend.view():

        list.insert(END,row)



def action():

    pass





date_label = Label(win, text = 'Date').grid(row =0, column = 1)

date_entry = Entry(win, textvariable = date)
date_entry.grid(row = 0, column = 2)


earn_label = Label(win, text = 'Earnings').grid(row =1, column = 1)

earn_entry = Entry(win, textvariable = earn)
earn_entry.grid(row = 1, column = 2)


excerise_label = Label(win, text = 'Excerise').grid(row =2, column = 1)

excerise_entry = Entry(win, textvariable = excerise)
excerise_entry.grid(row = 2, column = 2)


study_label = Label(win, text = 'Study').grid(row =0, column = 3)

study_entry = Entry(win, textvariable = study)
study_entry.grid(row = 0, column = 4)


diet_label = Label(win, text = 'Diet').grid(row =1, column = 3)

diet_entry = Entry(win, textvariable = diet)
diet_entry.grid(row = 1, column = 4)


python_label = Label(win, text = 'Python').grid(row =2, column =3)

python_entry = Entry(win, textvariable = python)
python_entry.grid(row = 2, column = 4)

box = Listbox(win,height=8,width=35)
box.grid(row=3,column=1,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=3 ,rowspan=9)

box.bind('<<ListboxSelection>' , get_selected_row) 

add_b = Button(win, text = 'ADD', command = add_command).grid(row = 3, column = 4)

search_b=  Button(win, text = 'SEARCH', command = action, width = 8).grid(row = 4, column = 4)

delete_b = Button(win, text = 'DELETE', command = delete_command, width = 8).grid(row = 5, column = 4)

view_b = Button(win, text = 'VIEW ALL', command = view_command, width = 8).grid(row = 6, column = 4)

clos_b = Button(win, text = 'CLOSE', command = win.destroy, width = 8).grid(row = 7, column = 4)



win.mainloop()