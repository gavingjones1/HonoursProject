from tkinter import *
from tkinter import ttk
from Ransomware import Append, Remove

def explanation():
    
    output.insert(END, '\n')
    output.insert(END, '\n')
    output.insert(END, '---------------------------------- \n')
    output.insert(END, '\n')
    output.insert(END, 'So as you can see, this kind of message could be very worrying for users to recieve. \n')
    output.insert(END, '\n')
    output.insert(END, 'If you look at the files on your desktop, you will see they have the extension ".ddd". \n')
    output.insert(END, '\n')
    output.insert(END, 'This is what the WANNACRY Ransomware attack on the NHS in 2017 looked like. This was all taken from a real life example. \n')
    output.insert(END, '\n')
    output.insert(END, 'Hit "Decrypt" below, and the files will go back to normal and an explanation will be displayed.')

def decrypt():
    output.delete(0.0, END)
    output.insert(END, 'So the WANNACRY ransomware attack cost the NHS millions. This attack was delivered the same way this one was, through an email. \n')
    output.insert(END, '\n')
    output.insert(END, 'The reason this attack was so successful is because the attack took advantage of unpatched systems. \n')
    output.insert(END, '\n')
    output.insert(END, 'To avoid attacks like this, look for the signs of spam emails, and keep your systems updated.')
    output.insert(END, '\n')
    output.insert(END, 'Record your findind in your notes page, then close this window and return to your controller.')
#main
root = Tk()

#root.minsize(width=500, height=500)
#root.maxsize(width=500, height=500)
root.resizable(width=False, height=False)
root.title("Room42 Checker")
root.configure(bg="red")


#Photo
photo1 = PhotoImage(file="lock.png")
Label (root, image=photo1, bg="red") .grid(row = 0, columnspan = 5)

#create label

Label (root, text="Oops, your files have been encrypted!", bg="red", fg = "white", font = "none 18 bold") .grid(row = 0, column = 6, columnspan = 2)



#add buttons

Email1B = ttk.Button(root, text="Explanation", width=23, command=explanation)
Email1B.grid(row = 20, column = 6)

Email2B = ttk.Button(root, text="Decrypt", width=23, command=decrypt)
Email2B.grid(row = 20, column = 7)


#output box

output = Text(root, width=55, height=20, wrap=WORD, background="white")
output.grid(row = 2, rowspan = 15, column = 5, columnspan = 3, sticky = E)

output.insert(END, '>>What happened to my computer? \n')
output.insert(END, '\n')
output.insert(END, 'We have taken over all of your files by encrypting them. \n')
output.insert(END, '\n')
output.insert(END, '>>Can I get my files back? \n')
output.insert(END, '\n')
output.insert(END, 'Sure. We can guarantee they will be decrypted as soon as payment is recieved to the account below. \n')
output.insert(END, '\n')
output.insert(END, '>>How do I pay? \n')
output.insert(END, '\n')
output.insert(END, 'Payment is accepted in bitcoin only. You will need to check the current bitcoin price and buy some bit coin. \n')
output.insert(END, '\n')
output.insert(END, 'Dont worry. Hit explanation below.')


#entry = Entry(root, textvariable = ent, width = 25).grid(row = 9, column = 0)
#entryB = ttk.Button(root, text = "ok", width = 25).grid(row = 10, column = 0)




root.mainloop()
