# This will import all the widgets
# and modules which are available in
# tkinter and ttk module

import tkinter as tk
from tkinter.ttk import *
 
# creates a Tk() object
master = tk.Tk()

bar = " " * 80
btFont = 12
 
# sets the geometry of main
# root window
master.geometry("500x500")
#master.color("blue") 

# function to check the code
# from user entry 
# by clicking a button
def codeChecker (window, entry, nQuiz, rightAnswer):
    answ = entry.get()

    if answ == rightAnswer :
        outText = " " * 25 + "Codice corretto!" + " " * 25
        outColor = "green"
    else:
        outText = "Controlla il QUIZ "+ nQuiz + " e prova ancora!"
        outColor = "red"
    label = tk.Label(window, text= outText, fg=outColor, font=("Helvetica", 16))
    label.grid(row = int(nQuiz), column = 2, padx = 5, sticky="N")

def all_good(window,  entry1, entry2, entry3, ra1, ra2, ra3):
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    if  x1 == ra1  and  x2 == ra2  and  x3 == ra3 :
        output_T = "Il mondo è salvo! Grazie!"
        output_C = "green"
    else:
        output_T = "Non ti arrendere! Riprova"
        output_C = "red"
    label = tk.Label(window, text= output_T, fg= output_C, font=("Helvetica", 30))
    label.grid(row = 4, column = 1, columnspan = 2,  padx=30, pady=30)
 
# function to open a new window
# on a button click
def openWindowGroupA():
     
    # Toplevel object which will
    # be treated as a new window
    newWindowA = tk.Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindowA.title("Gruppo A - Controlla i tuoi codici")
 
    # sets the geometry of toplevel
    newWindowA.geometry("800x500")
 
    # A Label widget to show in toplevel

    newWindowA.configure(background="blue")

    welcome_label = tk.Label(newWindowA,
                          text="Ciao gruppo A! \n Controlla qui i tuoi codici:",
                          font=("Helvetica", 45), fg="#0000FF")
    welcome_label.grid(row=0, column=0, columnspan = 3,  padx=30, pady=30)

    # first code 
    entry1 = tk.Entry (newWindowA)
    entry1.grid(row=1, column=0, sticky="N", padx=5)
    button1 = tk.Button(newWindowA, 
                        text='CONTROLLO CODICE QUIZ 1', 
                        command = lambda: codeChecker(window = newWindowA, entry = entry1, nQuiz = 1, rightAnswer = "314"), 
                        fg="black", 
                        font=("Helvetica", btFont))
    button1.grid(row = 1, column = 1, sticky = "N")
    space1 = tk.Label(newWindowA, text= bar, font = ("Helvetica", 16))
    space1.grid(row = 1, column = 2, padx = 5, sticky="N")

    # second code
    entry2 = tk.Entry (newWindowA)
    entry2.grid(row=2, column=0, sticky="N", padx=5)
    button2 = tk.Button(newWindowA,
                        text='CONTROLLO CODICE QUIZ 2',
                        command = lambda: codeChecker(window = newWindowA, entry = entry2, nQuiz = 2, rightAnswer = "159"),
                        fg="black",
                        font=("Helvetica", btFont))
    button2.grid(row = 2, column = 1, sticky = "N")
    space2 = tk.Label(newWindowA, text= bar, font = ("Helvetica", 16))
    space2.grid(row = 2, column = 2, padx = 5, sticky="N")

    # third code
    entry3 = tk.Entry (newWindowA)
    entry3.grid(row=3, column=0, sticky="N", padx=5)
    button3 = tk.Button(newWindowA,
                        text='CONTROLLO CODICE QUIZ 3',
                        command = lambda: codeChecker(window = newWindowA, entry = entry3, nQuiz = 3, rightAnswer = "265"),
                        fg="black",
                        font=("Helvetica", btFont))
    button3.grid(row = 3, column = 1, sticky = "N")
    space3 = tk.Label(newWindowA, text= bar, font = ("Helvetica", 16))
    space3.grid(row = 3, column = 2, padx = 5, sticky="N")
    
    # final check
    button_all = tk.Button(newWindowA, 
                           text = "CONTROLLO FINALE", 
                           command= lambda: all_good(window = newWindowA,  entry1= entry1, entry2 = entry2, entry3 = entry3, ra1 = "314", ra2 = "159", ra3 = "265"),  
                           fg="black", 
                           font=("Helvetica", 10))
    button_all.grid(row = 4, column = 0,  padx=30, pady=30)

label = tk.Label(master,
              text ="Seleziona la tua squadra")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = tk.Button(master,
             text ="Gruppo A",
             command = openWindowGroupA)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
tk.mainloop()
