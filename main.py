import random
from tkinter import *

#Games
import games.rps as rps

def openRps():
    rps.openGame()


application = Tk()
application.geometry("600x600")
application.title("You Vs Ai")

selectlabel = Label(application, text="Please choose a game: ", font=("Arial", 18))
selectlabel.pack(padx=10, pady=10)

rpsbutton = Button(application, text="Rock Paper Scissors", font=("Arial", 18), command=openRps)
rpsbutton.place(x=20, y=300)

application.mainloop()