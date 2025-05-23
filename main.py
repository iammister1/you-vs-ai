import random
from tkinter import *

#Games
import rps
import guessinggame

def openRps():
    rps.openGame()

def openGG():
    guessinggame.openGame()


application = Tk()
application.geometry("600x600")
application.title("You Vs Ai")

selectlabel = Label(application, text="Please choose a game: ", font=("Arial", 18))
selectlabel.pack(padx=10, pady=10)

rpsbutton = Button(application, text="Rock Paper Scissors", font=("Arial", 18), command=openRps)
rpsbutton.place(x=20, y=300)

ggbutton = Button(application, text="Guessing Game", font=("Arial", 18), command=openGG)
ggbutton.place(x=20, y=400)

application.mainloop()