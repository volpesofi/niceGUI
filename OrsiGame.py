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
master.geometry("500x300")
master.configure(background="black")
master.title("Seleziona la tua squadra")

# function to check the code
# from user entry 
# by clicking a button
def codeChecker (window, entry, nQuiz, rightAnswer):
    answ = entry.get()

    if answ == rightAnswer :
        outText = " " * 25 + "Codice corretto!" + " " * 25
        outColor = "green"
    else:
        outText = "Controlla il QUIZ "+ str(nQuiz) + " e prova ancora!"
        outColor = "red"
    label = tk.Label(window, text= outText, fg=outColor, font=("Helvetica", 16))
    label.grid(row = int(nQuiz), column = 2, padx = 5, sticky="N")

def all_good(window,  entry1, entry2, entry3, ra1, ra2, ra3):
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    if  x1 == ra1  and  x2 == ra2  and  x3 == ra3 :
        output_T = "  Il mondo è salvo! Grazie!  "
        output_C = '#00FF7F'
    else:
        output_T = "  Non ti arrendere! Riprova.  "
        output_C = '#DC143C'
    label = tk.Label(window, text= output_T, fg= output_C, font=("Helvetica", 30))
    label.grid(row = 4, column = 1, columnspan = 2,  padx=30, pady=30)
 
# function to open a new window
# on a button click
# and check the codes
def openWindowGroup(group, color, code1, code2, code3):
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Gruppo" + group + " - Controlla i tuoi codici")
 
    # sets the geometry of toplevel
    newWindow.geometry("800x500")
 
    # A Label widget to show in toplevel

    newWindow.configure(background=color)

    welcome_label = tk.Label(newWindow,
                             text = "Ciao gruppo " + group + "! \n Controlla qui i tuoi codici:",
                             font = ("Helvetica", 45), 
                             fg   = color)
    welcome_label.grid(row=0, column=0, columnspan = 3,  padx=30, pady=30)

    # first code 
    entry1 = tk.Entry (newWindow)
    entry1.grid(row=1, column=0, sticky="N", padx=5)
    button1 = tk.Button(newWindow, 
                        text='CONTROLLO CODICE QUIZ 1', 
                        command = lambda: codeChecker(window = newWindow, entry = entry1, nQuiz = 1, rightAnswer = code1), 
                        fg="black", 
                        font=("Helvetica", btFont))
    button1.grid(row = 1, column = 1, sticky = "N")
    space1 = tk.Label(newWindow, text= bar, font = ("Helvetica", 16))
    space1.grid(row = 1, column = 2, padx = 5, sticky="N")

    # second code
    entry2 = tk.Entry (newWindow)
    entry2.grid(row=2, column=0, sticky="N", padx=5)
    button2 = tk.Button(newWindow,
                        text='CONTROLLO CODICE QUIZ 2',
                        command = lambda: codeChecker(window = newWindow, entry = entry2, nQuiz = 2, rightAnswer = code2),
                        fg="black",
                        font=("Helvetica", btFont))
    button2.grid(row = 2, column = 1, sticky = "N")
    space2 = tk.Label(newWindow, text= bar, font = ("Helvetica", 16))
    space2.grid(row = 2, column = 2, padx = 5, sticky="N")

    # third code
    entry3 = tk.Entry (newWindow)
    entry3.grid(row=3, column=0, sticky="N", padx=5)
    button3 = tk.Button(newWindow,
                        text='CONTROLLO CODICE QUIZ 3',
                        command = lambda: codeChecker(window = newWindow, entry = entry3, nQuiz = 3, rightAnswer = code3),
                        fg="black",
                        font=("Helvetica", btFont))
    button3.grid(row = 3, column = 1, sticky = "N")
    space3 = tk.Label(newWindow, text= bar, font = ("Helvetica", 16))
    space3.grid(row = 3, column = 2, padx = 5, sticky="N")
    
    # final check
    colorALL = '#FF6347' #'#ff7f00' 
    button_all = tk.Button(newWindow, 
                           text = "CONTROLLO FINALE", 
                           command= lambda: all_good(window = newWindow,  entry1= entry1, entry2 = entry2, entry3 = entry3, ra1 = code1, ra2 = code2, ra3 = code3),  
                           fg                  = colorALL,
                           bd                  = 10,
                           highlightthickness  = 4,
                           highlightcolor      = colorALL,
                           highlightbackground = colorALL,
                           borderwidth         = 4,
                           font                = ("Helvetica", 14))                           
    button_all.grid(row = 4, column = 0,  padx= 5, pady=30)


label = tk.Label(master,
              text = " Seleziona la tua squadra ",
              font = ("Helvetica", 26),
              bg = "black", fg = "white")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click

colorA = '#228b22'
btnA = tk.Button(master,
                 text                = 'Gruppo A',
                 fg                  = colorA,
                 bg                  = '#001d99',
                 bd                  = 10,
                 highlightthickness  = 4,
                 highlightcolor      = colorA,
                 highlightbackground = colorA,
                 borderwidth         = 4,
                 font                = ("Helvetica", 22),
                 command = lambda : openWindowGroup(group = "A", 
                                                    color = colorA, 
                                                    code1 = "314", code2 = "159", code3 = "265") )
btnA.pack(pady = 10)

colorB = '#9a32cd'
btnB = tk.Button(master,
                 text                = 'Gruppo B',
                 fg                  = colorB,
                 bg                  = '#001d99',
                 bd                  =  10,
                 highlightthickness  = 4,
                 highlightcolor      = colorB,
                 highlightbackground = colorB,
                 borderwidth         = 4,
                 font                = ("Helvetica", 22),
                 command = lambda : openWindowGroup(group = "B",
                                                    color = colorB,
                                                    code1 = "358", code2 = "979", code3 = "323") )
btnB.pack(pady = 10)

colorC = '#37d3ff'
btnC = tk.Button(master, 
                 text                = 'Gruppo C',
                 fg                  = colorC,
                 bg                  = '#001d99',
                 bd                  =  10, 
                 highlightthickness  = 4, 
                 highlightcolor      = colorC, 
                 highlightbackground = colorC, 
                 borderwidth         = 4,
                 font                = ("Helvetica", 22),
                 command = lambda : openWindowGroup(group = "C", 
                                                    color = colorC,
                                                    code1 = "846", code2 = "264", code3 = "338") )
btnC.pack(pady = 10)
 
# mainloop, runs infinitely
tk.mainloop()
