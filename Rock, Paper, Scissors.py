import tkinter as tk
from tkinter import messagebox
import random
CHOICES = ["Rock", "Paper", "Scissors"]
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You Win!"
    else:
        return "Computer Wins!"
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(CHOICES)
    result = determine_winner(user_choice, computer_choice)
    lbl_user_choice.config(text=f"Your Choice: {user_choice}")
    lbl_computer_choice.config(text=f"Computer's Choice: {computer_choice}")
    lbl_result.config(text=result)
    if result == "You Win!":
        user_score += 1
    elif result == "Computer Wins!":
        computer_score += 1
    lbl_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    lbl_user_choice.config(text="Your Choice: ")
    lbl_computer_choice.config(text="Computer's Choice: ")
    lbl_result.config(text="")
    lbl_score.config(text="Score - You: 0 | Computer: 0")
user_score = 0
computer_score = 0
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.resizable(False, False)
lbl_title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
lbl_title.pack(pady=10)
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
btn_rock = tk.Button(frame_buttons, text="Rock", width=10, command=lambda: play("Rock"))
btn_paper = tk.Button(frame_buttons, text="Paper", width=10, command=lambda: play("Paper"))
btn_scissors = tk.Button(frame_buttons, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_rock.grid(row=0, column=0, padx=5)
btn_paper.grid(row=0, column=1, padx=5)
btn_scissors.grid(row=0, column=2, padx=5)
lbl_user_choice = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
lbl_user_choice.pack()
lbl_computer_choice = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
lbl_computer_choice.pack()
lbl_result = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
lbl_result.pack(pady=10)
lbl_score = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
lbl_score.pack()
btn_reset = tk.Button(root, text="Reset Game", command=reset_game, bg="orange", width=15)
btn_reset.pack(pady=10)
btn_exit = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", width=15)
btn_exit.pack()
root.mainloop()
