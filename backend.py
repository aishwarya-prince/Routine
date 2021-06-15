import backend
from tkinter import *
import tkinter as tk

#creating the Tkinter window
win = Tk()
win.title("Moody")
win.config(background="light blue")

#declaring all the nesscessary variables
date = tk.StringVar()
earn = tk.StringVar()
excerise = tk.StringVar()
study = tk.StringVar()
diet = tk.StringVar()
python = tk.StringVar()
status = tk.StringVar()

#this function is called when cursor clicks on any row in listbox
def showSelected(event):
    global itm
    selected = lis.curselection()[0]
    itm = lis.get(selected)
    print(itm)

    #when any row is clicked, entry boxes get updated
    date_entry.delete(0,END)
    date_entry.insert(END,itm[1])
    print(itm)
    earn_entry.delete(0,END)
    earn_entry.insert(END,itm[2])
    print(itm[1])
    excerise_entry.delete(0,END)
    excerise_entry.insert(END,itm[3])
    study_entry.delete(0,END)
    study_entry.insert(END,itm[4])
    diet_entry.delete(0,END)
    diet_entry.insert(END,itm[5])
    python_entry.delete(0,END)
    python_entry.insert(END,itm[6])

#function called from Delete button
def delete_command():
    backend.delete(itm[0])
    lis.delete(0, END)
    date_entry.delete(0,END)
    earn_entry.delete(0,END)
    excerise_entry.delete(0,END)
    study_entry.delete(0,END)
    diet_entry.delete(0,END)
    python_entry.delete(0,END)

    #adding appropriate text in entry boxes
    status_entry.delete(0,END)
    status_entry.insert( END, f"Entry of {itm[1]} deleted")

    #adding rest of the non deleted rows in Listbox
    for row in backend.view():
        lis.insert(END,row)

#called when add button is clicked
def add_command():
    #making sure if all the entry box are filled
    if date.get() == "" or earn.get() == "" or excerise.get() == "" or study.get() == "" or diet.get() == "" or python.get() == "":
        status_entry.delete(0,END)
        status_entry.insert( END, "Please fill all the boxes") 

    #Sending values added to entryboxes to Backend code and storing it in Database
    else:
        backend.insert(date.get(), earn.get(), excerise.get(), study.get(), diet.get(), python.get())
        lis.delete(0,END)
        lis.insert(END,(date.get(),earn.get(),excerise.get(),study.get(),diet.get(),python.get()))
        status_entry.delete(0,END)
        status_entry.insert( END, f"Entry of {date.get()} is added")

#called when view button is clicked
def view_command():
    #deleting the contents present in listbox and adding all the values stored in Database
    lis.delete(0, END)
    for row in backend.view():
        lis.insert(END,row)

    status_entry.delete(0,END)
    status_entry.insert( END, "showing all the entries in Database")

#called when search button is clicked
def search_command():
    lis.delete(0, END)

    #sending data in entry boxes to backend and displaying stored values in DB as per the search 
    for row in backend.search(date.get(), earn.get(), excerise.get(), study.get(), diet.get(), python.get()):
        lis.insert(END,row)    
    status_entry.delete(0,END)
    status_entry.insert( END, "showing all the entries in Database for the above search")

#called when close button is pressed, closes the tkinter window
def close_command():
    win.destroy()

#configuring buttons, labels, entry boxes, scroolbar , listbox     
date_label = Label(win, text = 'Date', bg="light blue",font = ('Courier',11,'bold'),width = 12).grid(row =0, column = 1)
date_entry = Entry(win, textvariable = date,font = ('cambria',12,'italic'), width=30)
date_entry.grid(row = 0, column = 2,sticky=W)

earn_label = Label(win, text = 'Earnings', bg="light blue",font = ('Courier',11,'bold'),width = 12).grid(row =1, column = 1)
earn_entry = Entry(win, textvariable = earn, font = ('cambria',12,'italic'), width=30)
earn_entry.grid(row = 1, column = 2,sticky=W)

excerise_label = Label(win, text = 'Excerise', bg="light blue",font = ('Courier',11,'bold'),width = 12).grid(row =2, column = 1)
excerise_entry = Entry(win, textvariable = excerise,font = ('cambria',12,'italic'), width=30)
excerise_entry.grid(row = 2, column = 2, sticky=W)

study_label = Label(win, text = 'Study', bg="light blue",font = ('Courier',11,'bold'),width = 12).grid(row =0, column = 3)
study_entry = Entry(win, textvariable = study, font = ('cambria',12,'italic'), width=30)
study_entry.grid(row = 0, column = 4)

diet_label = Label(win, text = 'Diet', bg="light blue",font = ('Courier',11,'bold'),width = 12).grid(row =1, column = 3)
diet_entry = Entry(win, textvariable = diet, font = ('cambria',12,'italic'), width=30)
diet_entry.grid(row = 1, column = 4)

python_label = Label(win, text = 'Python', bg="light blue",font = ('Courier',11,'bold')).grid(row =2, column =3)
python_entry = Entry(win, textvariable = python, font = ('cambria',12,'italic'), width=30)
python_entry.grid(row = 2, column = 4)

scroll = Scrollbar(win)

#binding listbox with scrllbar to its right
lis = Listbox(win, yscrollcommand = scroll.set, height=20, font = ('cambria',12,'italic'))
lis.grid(row=3,column=1,rowspan=10,columnspan=4, padx=10, pady=10, sticky=N+S+E+W)

scroll.grid( row = 3, column = 5, rowspan= 10, sticky=N+S+W)
scroll.config(command = lis.yview )

add_b = Button(win, text = 'ADD', command = add_command, width = 12,font = ('Times',10,'bold')).grid(row = 3, column = 6, pady=5, padx=5)
search_b=  Button(win, text = 'SEARCH', command = search_command, width = 12,font = ('Times',9,'bold')).grid(row = 4, column = 6, pady=5, padx=5)
delete_b = Button(win, text = 'DELETE', command = delete_command, width = 12,font = ('Times',10,'bold')).grid(row = 5, column = 6, pady=5, padx=5)
view_b = Button(win, text = 'VIEW ALL', command = view_command, width = 12,font = ('Times',10,'bold')).grid(row = 6, column = 6, pady=5, padx=5)
clos_b = Button(win, text = 'CLOSE', command = close_command, width = 12,font = ('Times',10,'bold')).grid(row = 7, column = 6, pady=5, padx=5)

#binding listbox with curseselection
lis.bind('<<ListboxSelect>>', showSelected)

state = Label(win, text = 'Status', bg="light blue",font = ('Courier',10,'bold')).grid(row =14, column = 1, pady=5)
status_entry = Entry(win, textvariable= status, font = ('cambria',10,'italic'))
status_entry.grid(row =14, column =2,columnspan=6, pady=5, padx=10, sticky=NSEW)

win.mainloop()
