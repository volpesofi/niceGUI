import tkinter as tk

#### root set up
root= tk.Tk()
root.title("Controlla i tuoi codici segreti!")
#root.geometry("900x550")


#### canvas group A ######  
convas_A = tk.Canvas(root, width = 800, height = 300)
convas_A.pack(expand = True)
convas_A.configure(background="blue")
#convas_A.columnconfigure(0, weight=1)
#convas_A.columnconfigure(1, weight=3)

welcome_label = tk.Label(convas_A,
                         text="Ciao gruppo A! \n Controlla qui i tuoi codici:",
                         font=("Helvetica", 45), fg= "magenta")
welcome_label.grid(row=0, column=0, columnspan = 3,  padx=30, pady=30)

entry1 = tk.Entry (convas_A) 
#convas_A.create_window( 100, 140, width = 100, window=entry1)
entry1.grid(row=1, column=0, sticky="N", padx=5)

entry2 = tk.Entry (convas_A)
#convas_A.create_window(100, 180, window=entry2)
entry2.grid(row=2, column=0, sticky="N", padx=5)

entry3 = tk.Entry (convas_A)
#convas_A.create_window(100, 220, window=entry3)
entry3.grid(row=3, column=0, sticky="N", padx=5)

def checkCode1 ():  
    x1 = entry1.get()
    
    if x1 == "314":
        text1 = " " * 25 + "Codice corretto!" + " " * 25
        color1 = "green" 
    else:
        text1 = "Controlla il QUIZ 1 e prova ancora"
        color1 = "red"
    label1 = tk.Label(convas_A, text= text1, fg=color1, font=("Helvetica", 16))
    label1.grid(row = 1, column = 2, padx = 5, sticky="N")
    #convas_A.create_window(600, 140, window=label1)

def checkCode2 ():
    x1 = entry2.get()

    if x1 == "159":
        text1 = " " * 25 + "Codice corretto!" + " " * 25
        color1 = "green"
    else:
        text1 = "Controlla il QUIZ 2 e prova ancora"
        color1 = "red"
    label1 = tk.Label(convas_A, text= text1, fg=color1, font=("Helvetica", 16))
    label1.grid(row = 2, column = 2, padx = 5, sticky="N")
    #convas_A.create_window(600, 180, window=label1)


def checkCode3():
    x1 = entry3.get()

    if x1 == "265":
        text1 = " " * 25 + "Codice corretto!" + " " * 25
        color1 = "green"
    else:
        text1 = "Controlla il QUIZ 3 e prova ancora"
        color1 = "red"
    label1 = tk.Label(convas_A, text= text1, fg=color1, font=("Helvetica", 16))
    label1.grid(row = 3, column = 2, padx = 5, sticky="N")

def all_good():
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    if  x1 == "314" and  x2 == "159" and  x3 == "265" :  
        output_T = "Il mondo è salvo! Grazie!"
        output_C = "green"
    else: 
        output_T = "Non ti arrendere! Riprova"
        output_C = "red"
    label = tk.Label(convas_A, text= output_T, fg= output_C, font=("Helvetica", 30))
    label.grid(row = 4, column = 1, columnspan = 2,  padx=30, pady=30)

    
bar = " " * 80

button1 = tk.Button(convas_A, text='CONTROLLO CODICE QUIZ 1', command=checkCode1, fg="black", font=("Helvetica", 10))
button1.grid(row = 1, column = 1, sticky = "N")
space1 = tk.Label(convas_A, text= bar, font=("Helvetica", 16))
space1.grid(row = 1, column = 2, padx = 5, sticky="N")


button2 = tk.Button(convas_A, text='CONTROLLO CODICE QUIZ 2', command=checkCode2, fg="black", font=("Helvetica", 10))
button2.grid(row = 2, column = 1, sticky = "N")
space2 = tk.Label(convas_A, text= bar, font=("Helvetica", 16))
space2.grid(row = 2, column = 2, padx = 5, sticky="N")

button3 = tk.Button(convas_A, text='CONTROLLO CODICE QUIZ 3', command=checkCode3, fg="black", font=("Helvetica", 10))
button3.grid(row = 3, column = 1, sticky = "N")
space3 = tk.Label(convas_A, text= bar, font=("Helvetica", 16))
space3.grid(row = 3, column = 2, padx = 5, sticky="N")

button_all = tk.Button(convas_A, text = "CONTROLLO FINALE", command=all_good,  fg="black", font=("Helvetica", 10))
button_all.grid(row = 4, column = 0,  padx=30, pady=30)


root.mainloop()
