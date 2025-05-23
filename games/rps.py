import random
from tkinter import *

def openGame():
    window = Toplevel()
    window.geometry("600x600")
    window.title("Rock Paper Scissors")

    rpslabel = Label(window, text="Rock Paper Scissors")
    rpslabel.pack(padx=10, pady=10)

    rockbutton = Button(window, text="Rock", font=("Arial", 18))
    rockbutton.pack(padx=10, pady=10)

    paperbutton = Button(window, text="Paper", font=("Arial", 18))
    paperbutton.pack(padx=10, pady=10)

    scissorsbutton = Button(window, text="Scissors", font=("Arial", 18))
    scissorsbutton.pack(padx=10, pady=10)