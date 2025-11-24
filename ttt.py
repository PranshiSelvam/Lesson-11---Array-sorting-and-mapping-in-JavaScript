import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Tic Tac Toe - User vs Laptop")

buttons = []
board = [""] * 9   
user_symbol = "X"
comp_symbol = "O"

def check_winner(symbol):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]            
    ]
    for wc in win_conditions:
        if board[wc[0]] == symbol and board[wc[1]] == symbol and board[wc[2]] == symbol:
            return True
    return False

def user_move(index):
    if board[index] == "":
        board[index] = user_symbol
        buttons[index].config(text=user_symbol, state="disabled")

        if check_winner(user_symbol):
            messagebox.showinfo("Game Over", "You WIN!! 🎉")
            reset_game()
            return

        if "" not in board:   
            messagebox.showinfo("Game Over", "It's a DRAW!")
            reset_game()
            return

        computer_move()

def computer_move():
    empty_cells = [i for i in range(9) if board[i] == ""]
    if not empty_cells:
        return

    comp_index = random.choice(empty_cells)
    board[comp_index] = comp_symbol
    buttons[comp_index].config(text=comp_symbol, state="disabled")

    if check_winner(comp_symbol):
        messagebox.showinfo("Game Over", "Laptop WINS! 🤖")
        reset_game()
        return

def reset_game():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: user_move(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
