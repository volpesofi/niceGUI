# This will import all the widgets
# and modules which are available in
# tkinter and ttk module

from tkinter import *
from tkinter.ttk import *
 
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("500x500")
 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Controlla i tuoi codici")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="Controllo codici").pack()
 
 
label = Label(master,
              text ="Seleziona la tua squadra")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Gruppo A",
             command = openNewWindow)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()
