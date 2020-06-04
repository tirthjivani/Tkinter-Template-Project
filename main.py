from tkinter import *
import tkinter.messagebox

def leftclick(event):
	print("Left Mouse Button clicked")

def rightclick(event):
	print("Right Mouse Button clicked")

def click(button):
	Button(button).bind("<Button-3>", rightclick)
	Button(button).bind("<Button-1>", leftclick)

# *** Main Menu ***

root = Tk()


tkinter.messagebox.showinfo("Windows Title", "Warning!!")
answer = tkinter.messagebox.askquestion("Question1", 'Do you like chocolates?')

if answer == "yes":
	print("Tirth")
else:
	print("!Tirth")

canavas = Canvas(root, width=200, height=200)
canavas.pack()

blackline = canavas.create_line(0, 0, 200, 100)
redline = canavas.create_line(0, 200, 200, 100, fill="Red")

canavas.delete(ALL)

greenline = canavas.create_line(200, 0, 0, 100, fill="green")
blueline = canavas.create_line(0, 100, 200, 200, fill="green")



menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="Account", menu=submenu)
submenu.add_command(label="Log In", command=click)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Quit", menu=editMenu)
editMenu.add_command(label="Exit", command=click)

# root.mainloop()

# *** Toolbar ***

toolbar = Frame(root, bg="blue")

insertBut = Button(toolbar, text="Insert")
insertBut.pack(side=LEFT, padx=2, pady=2)

printBut = Button(toolbar, text="Shit")
printBut.pack(side=LEFT, padx=2, pady=2)


toolbar.pack(side=TOP, fill=X)

text_in = Entry(root)
text_in.pack()

var = len(text_in.get())

# *** Status Bar ***
status = Label(root, text="Words Count : " + str(var), bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()