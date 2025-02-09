import tkinter as tk
from tkinter import messagebox
import random

# Function to get computer's choice
def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def user_choice_action(user_choice):
    comp_choice_text = computer_choice()
    result = determine_winner(user_choice, comp_choice_text)
    result_label.config(text=f"Computer chose: {comp_choice_text}")
    messagebox.showinfo("Result", result)

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Set window size
window.geometry("400x300")

# Title label
title_label = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Arial", 16))
title_label.pack(pady=20)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Buttons for user to choose Rock, Paper, or Scissors
rock_button = tk.Button(window, text="Rock", width=15, height=2, font=("Arial", 12), 
                        command=lambda: user_choice_action("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=15, height=2, font=("Arial", 12), 
                         command=lambda: user_choice_action("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, font=("Arial", 12), 
                             command=lambda: user_choice_action("Scissors"))
scissors_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
