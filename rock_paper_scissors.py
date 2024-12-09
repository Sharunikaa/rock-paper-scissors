import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]


def determine_winner(user_choice, computer_choice):
  """
  Determines the winner of the game based on user and computer choices.

  Args:
      user_choice: The user's choice (rock, paper, or scissors).
      computer_choice: The computer's choice (rock, paper, or scissors).

  Returns:
      A string indicating the winner ("user", "computer", or "tie").
  """
  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "user"
    else:
      return "computer"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "user"
    else:
      return "computer"
  else:
    if computer_choice == "paper":
      return "user"
    else:
      return "computer"


def play_game():
  """
  This function handles the game logic and updates the GUI elements.
  """
  global computer_choice_label, result_label
  computer_choice = random.choice(choices)
  winner = determine_winner(user_choice.get(), computer_choice)

  computer_choice_label.config(text=f"Computer chose: {computer_choice}")

  if winner == "user":
    result_label.config(text="You Win!")
  elif winner == "computer":
    result_label.config(text="You Lose!")
  else:
    result_label.config(text="It's a Tie!")


# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Title label
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20))
title_label.pack(pady=20)

# User choice selection frame
user_choice_frame = tk.Frame(root)
user_choice_frame.pack()

# User choice buttons
user_choice = tk.StringVar(root)
rock_button = tk.Button(
    user_choice_frame, text="Rock", command=lambda: user_choice.set("rock")
)
paper_button = tk.Button(
    user_choice_frame, text="Paper", command=lambda: user_choice.set("paper")
)
scissors_button = tk.Button(
    user_choice_frame, text="Scissors", command=lambda: user_choice.set("scissors")
)

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)

# Computer choice label
computer_choice_label = tk.Label(root, text="Computer's choice: ")
computer_choice_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Play button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
