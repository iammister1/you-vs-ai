import random
from tkinter import *

moves = ["Rock", "Paper", "Scissors"]
player_move = ""

def openGame():
    window = Toplevel()
    window.geometry("600x600")
    window.title("Rock Paper Scissors")

    def rbuttonPress():
        global player_move
        player_move = "Rock"
        disable_buttons()
        ready()

    def spress():
        global player_move
        player_move = "Scissors"
        disable_buttons()
        ready()

    def ppress():
        global player_move
        player_move = "Paper"
        disable_buttons()
        ready()

    def disable_buttons():
        rockbutton.config(state=DISABLED)
        paperbutton.config(state=DISABLED)
        scissorsbutton.config(state=DISABLED)

    def enable_buttons():
        rockbutton.config(state=NORMAL)
        paperbutton.config(state=NORMAL)
        scissorsbutton.config(state=NORMAL)

    def ready():
        random_move = random.choice(moves)
        
        result = "Tie!" if random_move == player_move else f"Ai chose {random_move}. You {('Win!' if (player_move, random_move) in [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')] else 'Lose!')}"

        result_label.config(text=result)
        reset_button.config(state=NORMAL)

    def reset_game():
        global player_move
        player_move = ""
        result_label.config(text="Choose your move:")
        enable_buttons()
        reset_button.config(state=DISABLED)

    rpslabel = Label(window, text="Rock Paper Scissors", font=("Arial", 18))
    rpslabel.pack(padx=10, pady=10)

    rockbutton = Button(window, text="Rock", font=("Arial", 18), command=rbuttonPress)
    rockbutton.pack(padx=10, pady=10)

    paperbutton = Button(window, text="Paper", font=("Arial", 18), command=ppress)
    paperbutton.pack(padx=10, pady=10)

    scissorsbutton = Button(window, text="Scissors", font=("Arial", 18), command=spress)
    scissorsbutton.pack(padx=10, pady=10)

    result_label = Label(window, text="Choose your move:", font=("Arial", 14))
    result_label.pack(pady=10)

    reset_button = Button(window, text="Play Again", font=("Arial", 14), command=reset_game, state=DISABLED)
    reset_button.pack(pady=10)
