from tkinter import *
import random

def welcome():

    global welcomesc
    welcomesc = Tk()

    icon = PhotoImage(file = 'welcomesheldon.png')
    welcomesheldon = PhotoImage(file = 'welcomesheldon.png')
    welcomesc.geometry("700x700")
    welcomesc.title("Rock - Paper - Scissors - Lizard - Spock")
    welcomesc.iconphoto(False, icon)
    welcomesc.config(background="black")
    welcomesc.resizable(False,False)

    welcometext = "Hi, this is AI Sheldon Cooper.\nYou might know me from The Big Bang Theory.\nLet's play one of my favorite games\ncalled rock paper scissors lizard Spock"

    frame = Frame(welcomesc, 
              height= 670, 
              width= 670, 
              background = "#5a8f60")
    frame2 = Frame(frame,
               height=666,
               width=666,
               background="black")
    label1 = Label(frame2, 
               text = welcometext, 
               font=("Courier New", 12, "bold"),
               fg = "#5a8f60",
               image = welcomesheldon,
               compound="bottom",
               background="black",)
    button1 = Button(frame2,
                     text="PLAY",
                     font=("Courier New", 12, "bold"),
                     bg = "#5a8f60",
                     fg = "black",
                     activebackground = "#5a8f60",
                     activeforeground = "black",
                     bd=0,
                     command= secondwindow)

    frame.pack(padx = 15 ,pady = 15)
    frame2.pack(padx = 4, pady= 4)
    frame2.pack_propagate(False)
    label1.pack(pady=30)
    button1.pack(pady=45)

    welcomesc.mainloop()

def secondwindow():

    geometry = welcomesc.geometry()
    welcomesc.destroy()
    global secondwindowsc
    secondwindowsc =  Tk()

    secondwindowsc.geometry(geometry)
    secondwindowsc.geometry("700x700")
    secondwindowsc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    secondwindowsc.iconphoto(False, icon)
    secondwindowsc.config(background="black")
    secondwindowsc.resizable(False,False)

    global x
    x = IntVar()

    label2 = Label(secondwindowsc, 
                text = "Do you know the rules?", 
                font=("Courier New", 18 , "bold"),
                fg = "#5a8f60",
                background="black")
    radiobutton1 = Radiobutton(secondwindowsc, 
                text="yes",
                value =1,
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,activebackground="black",
                activeforeground="black",
                variable = x,
                selectcolor="black")
    radiobutton2 = Radiobutton(secondwindowsc,
                text="no",
                value =0,
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,
                activebackground="black",
                activeforeground="black",
                variable = x,
                selectcolor="black")
    button2 = Button(secondwindowsc,
                text="NEXT",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command = rules)

    label2.pack(pady=150)
    radiobutton1.pack()
    radiobutton2.pack()
    button2.pack(pady=80)

    secondwindowsc.mainloop()

def rules():

    geometry = secondwindowsc.geometry()
    secondwindowsc.destroy()
    global rulessc
    rulessc =  Tk()

    rulessc.geometry(geometry)
    rulessc.geometry("700x700")
    rulessc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    rulessc.iconphoto(False, icon)
    rulessc.config(background="black")
    rulessc.resizable(False,False)

    rulestext = "It's very simple.\nScissors cuts paper,\npaper covers rock,\nrock crushes lizard,\nlizard poisons Spock,\nSpock smashes scissors,\nscissors decapitates lizard,\nlizard eats paper,\npapaer disproves Spock,\nSpock vaporized rock,\nand as it always has,\nrock crushes scissors."

    label3 = Label(rulessc, 
                text = rulestext, 
                font=("Courier New", 18 , "bold"),
                fg = "#5a8f60",
                background="black")
    button3 = Button(rulessc,
                text="NEXT",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command=rulesdes)

    global  geometryrul
    geometryrul = rulessc.geometry()

    if(x.get()==0):
        label3.pack(pady=80)
        button3.pack(pady= 40)
    elif(x.get()==1):
        rulesdes()

    rulessc.mainloop()

def rulesdes():

    rulessc.destroy()
    choosing()

def choosing():
  
    global choosingsc
    choosingsc =  Tk()

    choosingsc.geometry(geometryrul)
    choosingsc.geometry("700x700")
    choosingsc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    choosingsc.iconphoto(False, icon)
    choosingsc.config(background="black")
    choosingsc.resizable(False,False)

    global c
    c = StringVar()

    radiobutton10 = Radiobutton(choosingsc, 
                text="rock",
                value ="rock",
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,activebackground="black",
                activeforeground="black",
                variable = c,
                selectcolor="black")
    radiobutton11 = Radiobutton(choosingsc, 
                text="paper",
                value ="paper",
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,activebackground="black",
                activeforeground="black",
                variable = c,
                selectcolor="black")
    radiobutton12 = Radiobutton(choosingsc, 
                text="scissors",
                value ="scissors",
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,activebackground="black",
                activeforeground="black",
                variable = c,
                selectcolor="black")
    radiobutton13 = Radiobutton(choosingsc, 
                text="lizard",
                value ="lizard",
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,activebackground="black",
                activeforeground="black",
                variable = c,
                selectcolor="black")
    radiobutton14 = Radiobutton(choosingsc, 
                text="Spock",
                value ="Spock",
                font=("Courier New", 18, "bold"),
                background="black",
                foreground="#5a8f60",
                width=10,activebackground="black",
                activeforeground="black",
                variable = c,
                selectcolor="black")
    label4 = Label(choosingsc, 
                text = "Choose one:", 
                font=("Courier New", 18 , "bold"),
                fg = "#5a8f60",
                background="black")
    button4 = Button(choosingsc,
                text="RESULT",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command=result)
    
    label4.pack(pady=50)
    radiobutton10.pack()
    radiobutton11.pack()
    radiobutton12.pack()
    radiobutton13.pack()
    radiobutton14.pack()
    button4.pack(pady=100)
    
    choosingsc.mainloop()

def result():

    choices = ["rock","paper","scissors","lizard","Spock"]
    global s
    s = random.choice(choices)
    y = c.get()

    def result(y,s):
        if s == "paper" and y == "scissors" or s == "rock" and y == "paper" or s == "lizard" and y == "rock" or s == "Spock" and y == "lizard" or s == "scissors" and y == "Spock" or s == "lizard" and y == "scissors" or s == "paper" and y == "lizard" or s == "Spock" and y == "paper" or s == "rock" and y == "Spock" or s == "scissors" and y == "rock":
            return(True)
        
    if y == s:
        print(tie())
   
    elif result(y,s):
        print(win())
            
    elif result(s,y):
        print(loose())

def win():

    geometry = choosingsc.geometry()
    choosingsc.destroy()
    global resultsc
    resultsc =  Tk()

    resultsc.geometry(geometry)
    resultsc.geometry("700x700")
    resultsc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    resultsc.iconphoto(False, icon)
    resultsc.config(background="black")
    resultsc.resizable(False,False)

    sadsheldon = PhotoImage(file = "sadsheldon.png")

    labelw = Label(resultsc, 
                text = ("You won, Sheldon chose "+ s), 
                font=("Courier New", 20, "bold"),
                fg = "#5a8f60",
                image = sadsheldon ,
                compound="bottom",
                background="black")
    buttone = Button(resultsc,
                text="PLAY AGAIN",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command= playagain)
    buttonb = Button(resultsc,
                text="END",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command= bye)
    
    labelw.pack(pady=30)
    buttone.pack(pady=30)
    buttonb.pack(pady=30)

    resultsc.mainloop()

def loose():

    geometry = choosingsc.geometry()
    choosingsc.destroy()
    global resultsc
    resultsc =  Tk()

    resultsc.geometry(geometry)
    resultsc.geometry("700x700")
    resultsc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    resultsc.iconphoto(False, icon)
    resultsc.config(background="black")
    resultsc.resizable(False,False)

    happysheldon = PhotoImage(file='happysheldon.png')

    labell = Label(resultsc, 
               text = ("You lost, Sheldon chose "+s), 
               font=("Courier New", 20, "bold"),
               fg = "#5a8f60",
               image = happysheldon,
               compound="bottom",
               background="black")
    buttone = Button(resultsc,
                text="PLAY AGAIN",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command= playagain)
    buttonb = Button(resultsc,
                text="END",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command= bye)
    
    labell.pack(pady=30)
    buttone.pack(pady=30)
    buttonb.pack(pady=30)

    resultsc.mainloop()

def tie():
    
    geometry = choosingsc.geometry()
    choosingsc.destroy()
    global resultsc
    resultsc =  Tk()
    resultsc.geometry(geometry)
    resultsc.geometry("700x700")
    resultsc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    resultsc.iconphoto(False, icon)
    resultsc.config(background="black")
    resultsc.resizable(False,False)

    tiesheldon = PhotoImage(file='tiesheldon.png')

    labelt = Label(resultsc, 
                text = ("Tie!"), 
                font=("Courier New", 20, "bold"),
                fg = "#5a8f60",
                image = tiesheldon,
                compound="bottom",
                background="black")
    buttone = Button(resultsc,
                text="PLAY AGAIN",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command= playagain)
    buttonb = Button(resultsc,
                text="END",
                font=("Courier New", 12, "bold"),
                bg = "#5a8f60",
                fg = "black",
                activebackground = "#5a8f60",
                activeforeground = "black",
                bd=0,
                command= bye)
            
    labelt.pack(pady=30)
    buttone.pack(pady=30)
    buttonb.pack(pady=30)

    resultsc.mainloop()  

def playagain():
    
    resultsc.destroy()
    choosing()

def bye():
    
    geometry =  resultsc.geometry()
    resultsc.destroy()
    global byesc
    byesc =  Tk()

    byesc.geometry(geometry)
    byesc.geometry("700x700")
    byesc.title("Rock - Paper - Scissors - Lizard - Spock")
    icon = PhotoImage(file = 'welcomesheldon.png')
    byesc.iconphoto(False, icon)
    byesc.config(background="black")
    byesc.resizable(False,False)

    byesheldon = PhotoImage(file='welcomesheldon.png')

    frameb = Frame(byesc, 
              height= 670, 
              width= 670, 
              background = "#5a8f60")
    frame2b = Frame(frameb,
               height=666,
               width=666,
               background="black")
    label1b = Label(frame2b, 
               text = "Thank You for the game, byeee :)", 
               font=("Courier New", 16, "bold"),
               fg = "#5a8f60",
               image = byesheldon,
               compound="bottom",
               background="black",)
   
    frameb.pack(padx = 15 ,pady = 15)
    frame2b.pack(padx = 4, pady= 4)
    frame2b.pack_propagate(False)
    label1b.pack(pady=65)
    
    byesc.mainloop()  

welcome()    