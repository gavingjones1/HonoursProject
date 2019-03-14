#tkinter for Final App
from tkinter import *

def tki():
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

    websiteB = Button(root, text="Website", width=25, command=printer)
    websiteB.grid(row = 3, column = 0)

    FileB = Button(root, text="Check Files", width=25, command=FileCheck)
    FileB.grid(row = 4, column = 0)

    ReplaceB = Button(root, text="Replace Files", width=25, command=FileReplace)
    ReplaceB.grid(row = 5, column = 0)

    EmailB = Button(root, text="Check Emails", width = 25, command=EmailCheck)
    EmailB.grid(row=6, column = 0)

    ClearB = Button(root, text="Clear", width=25, command=clear)
    ClearB.grid(row = 7, column = 0)


    #output box
    output = Text(root, width=50, height=20, wrap=WORD, background="white")
    output.grid(row = 3, rowspan = 15, column = 5, columnspan = 10, sticky = E)





    root.mainloop()

