import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import requests

# Kartenwerte und -farben
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [f"{value}_of_{suit}" for value in values for suit in suits]

# Verzeichnis für die Kartenbilder erstellen
os.makedirs('cards', exist_ok=True)

# Bilder herunterladen und speichern
for value in values:
    for suit in suits:
        if value == '10':
            value = '0'  # Anpassung für die Deck of Cards API
        url = f"https://deckofcardsapi.com/static/img/{value}{suit[0]}.png"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"cards/{value}_of_{suit}.png", 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download {value}_of_{suit}.png")

# Funktion zum Mischen des Decks
def shuffle_deck():
    random.shuffle(deck)

# Funktion zum Ziehen einer Karte
def draw_card():
    return deck.pop()

# Funktion zum Berechnen der Punktzahl
def calculate_score(hand):
    score = sum(values[card.split('_')[0]] for card in hand)
    if score > 21 and any(card.startswith('A') for card in hand):
        score -= 10
    return score

# Funktion zum Starten eines neuen Spiels
def new_game():
    global player_hand, dealer_hand
    shuffle_deck()
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]
    update_display()

# Funktion zum Aktualisieren der Anzeige
def update_display():
    player_score.set(f"Player: {calculate_score(player_hand)}")
    dealer_score.set(f"Dealer: {calculate_score(dealer_hand)}")
    
    for widget in player_frame.winfo_children():
        widget.destroy()
    for widget in dealer_frame.winfo_children():
        widget.destroy()
    
    for card in player_hand:
        card_image = Image.open(os.path.join("cards", f"{card}.png"))
        card_image = card_image.resize((100, 150), Image.LANCZOS)
        card_photo = ImageTk.PhotoImage(card_image)
        label = tk.Label(player_frame, image=card_photo)
        label.image = card_photo
        label.pack(side=tk.LEFT, padx=5, pady=5)
    
    for card in dealer_hand:
        card_image = Image.open(os.path.join("cards", f"{card}.png"))
        card_image = card_image.resize((100, 150), Image.LANCZOS)
        card_photo = ImageTk.PhotoImage(card_image)
        label = tk.Label(dealer_frame, image=card_photo)
        label.image = card_photo
        label.pack(side=tk.LEFT, padx=5, pady=5)

# Funktion für den "Hit"-Button
def hit():
    player_hand.append(draw_card())
    if calculate_score(player_hand) > 21:
        messagebox.showinfo("Blackjack", "Player busts! Dealer wins.")
        new_game()
    else:
        update_display()

# Funktion für den "Stand"-Button
def stand():
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card())
    update_display()
    if calculate_score(dealer_hand) > 21 or calculate_score(player_hand) > calculate_score(dealer_hand):
        messagebox.showinfo("Blackjack", "Player wins!")
    else:
        messagebox.showinfo("Blackjack", "Dealer wins!")
    new_game()

# GUI erstellen
root = tk.Tk()
root.title("Blackjack")
root.geometry("500x600")

player_hand = []
dealer_hand = []

player_score = tk.StringVar()
dealer_score = tk.StringVar()

tk.Label(root, textvariable=player_score, font=("Helvetica", 14)).pack(pady=10)
player_frame = tk.Frame(root)
player_frame.pack(pady=10)

tk.Label(root, textvariable=dealer_score, font=("Helvetica", 14)).pack(pady=10)
dealer_frame = tk.Frame(root)
dealer_frame.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Hit", command=hit, width=10).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Stand", command=stand, width=10).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="New Game", command=new_game, width=20).pack(pady=10)

new_game()
root.mainloop()