import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x475")
        self.root.config(bg="#2C2F33")  # Dunkler Hintergrund

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        # Label für den aktuellen Spieler
        self.player_label = tk.Label(
            self.root, text="Spieler: X", font=("Helvetica", 16, "bold"),
            bg="#2C2F33", fg="#FFFFFF"
        )
        self.player_label.pack(pady=10)

        # Spielfeld erstellen
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        board_frame = tk.Frame(self.root, bg="#2C2F33")
        board_frame.pack()

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    board_frame, text="", font=("Helvetica", 20, "bold"), width=5, height=2,
                    bg="#99AAB5", fg="#23272A", activebackground="#7289DA", 
                    activeforeground="#FFFFFF", command=lambda r=row, c=col: self.on_click(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

        # Neustart-Button
        self.restart_button = tk.Button(
            self.root, text="Neustart", font=("Helvetica", 14), bg="#7289DA", 
            fg="#FFFFFF", relief="flat", command=self.reset_game
        )
        self.restart_button.pack(pady=10)

    def on_click(self, row, col):
        # Überprüfen, ob das Feld leer ist
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # Überprüfen, ob jemand gewonnen hat
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            elif self.is_draw():
                self.show_winner("Draw")
            else:
                # Spieler wechseln
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_label.config(text=f"Spieler: {self.current_player}")

    def check_winner(self, player):
        # Zeilen, Spalten und Diagonalen überprüfen
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Zeile
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Spalte
                return True
        if all(self.board[i][i] == player for i in range(3)):      # Diagonale \
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Diagonale /
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def show_winner(self, result):
        # Disable alle Buttons
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

        # Schriftfarbe basierend auf Ergebnis
        if result == "X":
            color = "#43B581"  # Grün
            message = "Winner is X!"
        elif result == "O":
            color = "#F04747"  # Rot
            message = "Winner is O!"
        else:  # Unentschieden
            color = "#FFFFFF"  # Weiß
            message = "Draw!"

        # Gewinneranzeige
        self.winner_label = tk.Label(
            self.root, text=message, font=("Helvetica", 24, "bold"),
            bg="#2C2F33", fg=color
        )
        self.winner_label.pack(pady=20)

    def reset_game(self):
        # Spielfeld und Buttons zurücksetzen
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.player_label.config(text="Spieler: X")

        for row in self.buttons:
            for button in row:
                button.config(text="", state="normal")
        
        # Entferne Gewinneranzeige
        if hasattr(self, 'winner_label'):
            self.winner_label.config(text="")

# Hauptanwendung starten
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
