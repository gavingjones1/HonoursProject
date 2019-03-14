#SMILE Room 42 scenario checker
#Created by Gavin Jones
#Checks for: Access to specified websites, Files are in place, Email account is active.
#Can replace files if necassary to their original state

from tkinter import *
from tkinter import ttk

#from FileCheck import FileChecker, FileReplace
#from Website import website
from Emails import sendEmail1, sendEmail2, sendEmail3, deleteEmail,deleteEmail2
import time

file = open('export.txt', 'w')

#Functions

def Email1():
    sendEmail1()

def Email2():
    sendEmail2()

def Email3():
    sendEmail3()

def DelEmail():
    deleteEmail()
    
def DelEmail2():
    deleteEmail2()
    


#Clears the TKinter text box
def clear():
    output.delete(0.0, END)

#NOT WORKING YET - needs to run all commands.
def BigB():
    
    WebPrinter()
    
    FilePrinter()
    
    EmailPrinter()
    
    FileReplacePrinter()

    file.close()
#os.path.join - look it up




#########################################

#main
root = Tk()

#root.minsize(width=500, height=500)
#root.maxsize(width=500, height=500)
root.resizable(width=False, height=False)
root.title("Room42 Checker")
root.configure(bg="black")


#Photo
photo1 = PhotoImage(file="image.gif")
Label (root, image=photo1, bg="black") .grid(row = 0, columnspan = 6)

#create label
Label (root, text="What function would you like to carry out?", bg="black", fg = "white", font = "none 11 bold") .grid(row = 1, column = 0, columnspan = 3)


#create text entry box


#add buttons

Email1B = ttk.Button(root, text="Send first email", width=25, command=Email1)
Email1B.grid(row = 3, column = 0)

Email2B = ttk.Button(root, text="Send second email", width=25, command=Email2)
Email2B.grid(row = 4, column = 0)

Email3B = ttk.Button(root, text="Send third email", width=25, command=Email3)
Email3B.grid(row = 5, column = 0)

Email4B = ttk.Button(root, text="Delete Emails (dev)", width = 25, command=DelEmail)
Email4B.grid(row=6, column = 0)


Email5B = ttk.Button(root, text="Delete Emails 2 (dev)", width = 25, command=DelEmail2)
Email5B.grid(row=7, column = 0)


#output box

output = Text(root, width=50, height=20, wrap=WORD, background="white")
output.grid(row = 3, rowspan = 15, column = 5, columnspan = 10, sticky = E)


#entry = Entry(root, textvariable = ent, width = 25).grid(row = 9, column = 0)
#entryB = ttk.Button(root, text = "ok", width = 25).grid(row = 10, column = 0)




root.mainloop()
