import random
from tkinter import *

def openGame():
    window = Toplevel()
    window.geometry("600x600")
    window.title("Guessing Game")

    def only_numbers(char):
        return char.isdigit()
    
    validate_cmd = window.register(only_numbers)
    
    def afterinputenterbutton():
        random_number = random.randint(1,100)

        player_answer = playerinput.get()

        if player_answer == random_number:
            correct.pack()
            window.after(1000, correct.pack_forget())
        else:
            wrong.pack()
            window.after(1000, wrong.pack_forget)

    heading = Label(window, text="Choose a number between 1 and 100!", font=("Arial,", 18))
    heading.pack()

    playerinput = Entry(window, font=("Arial", 18), validate="key", validatecommand=(validate_cmd, "%S"))
    playerinput.pack(padx=40, pady=40)
    enterbutton = Button(window, text="Enter", font=("Arial", 18), command=afterinputenterbutton)
    enterbutton.pack(padx=10, pady=10)
    wrong = Label(window, text="Nope!", font=("Arial", 16))
    correct = Label(window, text="Correct!", font=("Arial", 18))
    higher = Label(window, text="Higher!", font=("Arial", 16))
    lower = Label(window, text="Lower!", font=("Arial", 18))
    
