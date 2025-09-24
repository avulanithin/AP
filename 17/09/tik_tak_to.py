# create a tik tak to gamee using tkinter and add make a bot to play against the user and make it smart so that the user cannot win
import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:  
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")
        master.geometry("400x400")
        master.resizable(False, False)

        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False

        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(master, text=" ", font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

        self.status_label = tk.Label(master, text="Player X's turn", font=('Arial', 16))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", font=('Arial', 12), command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=5)

    def make_move(self, index):
        if self.board[index] == " " and not self.game_over:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.status_label.config(text=f"Player {self.current_player} wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif " " not in self.board:
                self.status_label.config(text="It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
                if self.current_player == "O":
                    self.bot_move()

    def bot_move(self):
        # Simple AI: Choose a random empty spot
        empty_spots = [i for i in range(9) if self.board[i] == " "]
        if empty_spots:
            index = random.choice(empty_spots)
            self.make_move(index)

    def check_winner(self, player):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ")
        self.status_label.config(text="Player X's turn")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
