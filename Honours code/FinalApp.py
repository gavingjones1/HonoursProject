#Gavin Jones Honours project control app
#Created by Gavin Jones
#Controlling the incident scenario

from tkinter import *
from tkinter import ttk

#from FileCheck import FileChecker, FileReplace
#from Website import website
from Emails import sendEmailKey, sendEmailPhish, sendEmailRans, deleteEmailInbox, deleteEmailSent
import time

#Functions

def Email1():
    output.delete(0.0, END)
    output.insert(END, 'Please check your email. You will find an email there labelled ** and instructions going forward.')
    sendEmailKey()

def Email2():
    output.delete(0.0, END)
    output.insert(END, 'Well done for completing part one. Now again, please check your email. You will find an email there labelled ** and instructions going forward.')
    sendEmailPhish()

def Email3():
    output.delete(0.0,END)
    output.insert(END, 'Well done for completing part two. Now again, please check your email. You will find an email there labelled ** and instructions going forward.')
    sendEmailRans()

def DelEmailInbox():
    deleteEmailInbox()
    
def DelEmailSent():
    deleteEmailSent()
    


#Clears the TKinter text box
def clear():
    output.delete(0.0, END)

#NOT WORKING YET - needs to run all commands.
def BigB():
    
    WebPrinter()
    
    FilePrinter()
    
    EmailPrinter()
    
    FileReplacePrinter()

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
Label (root, text="Please select your task", bg="black", fg = "white", font = "none 11 bold") .grid(row = 1, column = 0, columnspan = 3)


#create text entry box


#add buttons

Email1B = ttk.Button(root, text="Part one", width=25, command=Email1)
Email1B.grid(row = 3, column = 0)

Email2B = ttk.Button(root, text="Part two", width=25, command=Email2)
Email2B.grid(row = 4, column = 0)

Email3B = ttk.Button(root, text="Part three", width=25, command=Email3)
Email3B.grid(row = 5, column = 0)

Email4B = ttk.Button(root, text="Delete Emails (dev)", width = 25, command=DelEmailInbox)
Email4B.grid(row=6, column = 0)


Email5B = ttk.Button(root, text="Delete Emails 2 (dev)", width = 25, command=DelEmailSent)
Email5B.grid(row=7, column = 0)


#output box

output = Text(root, width=50, height=20, wrap=WORD, background="white")
output.grid(row = 3, rowspan = 15, column = 5, columnspan = 10, sticky = E)

output.insert(END, 'This is your controller. The buttons on the left control the simulation. ')
output.insert(END, 'Proceed through each part, following respective instructions and dont forget to ')
output.insert(END, 'record your findings!')

#entry = Entry(root, textvariable = ent, width = 25).grid(row = 9, column = 0)
#entryB = ttk.Button(root, text = "ok", width = 25).grid(row = 10, column = 0)




root.mainloop()
