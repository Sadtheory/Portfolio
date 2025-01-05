import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk  # Pillow-Bibliothek für Bildverarbeitung

# Erstellen Sie einen neuen ChatBot
chatbot = ChatBot('KomplimentBot', 
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3',
                  logic_adapters=[
                      'chatterbot.logic.BestMatch'
                  ])

# Trainer für den ChatBot
trainer = ChatterBotCorpusTrainer(chatbot)

# Trainieren Sie den ChatBot mit dem deutschen Corpus-Datensatz
trainer.train("chatterbot.corpus.german")

# Liste der Komplimente und Fragen
komplimente = [
    "Du siehst heute großartig aus!",
    "Du bist unglaublich talentiert!",
    "Du hast ein wunderbares Lächeln!",
    "Du bist sehr intelligent!",
    "Du bist ein toller Freund!",
    "Du machst die Welt zu einem besseren Ort!",
    "Deine Kreativität ist beeindruckend!",
    "Du hast ein großes Herz!",
    "Du bist eine Inspiration für andere!",
    "Du hast eine tolle Ausstrahlung!",
    "Du bist sehr mutig!",
    "Du bist ein großartiger Zuhörer!",
    "Du hast einen tollen Sinn für Humor!",
    "Du bist sehr einfühlsam!",
    "Du bist ein wunderbarer Mensch!",
    "Du hast eine positive Einstellung!",
    "Du bist sehr hilfsbereit!",
    "Du bist ein echtes Vorbild!"
]

fragen = [
    "Wie schaffst du es, immer so positiv zu bleiben?",
    "Was ist dein Geheimnis für so viel Erfolg?",
    "Wie bist du so gut in dem, was du tust?",
    "Was inspiriert dich jeden Tag?",
    "Wie bleibst du immer so motiviert?",
    "Was ist dein Lieblingskompliment, das du je bekommen hast?",
    "Wie schaffst du es, immer so freundlich zu sein?",
    "Was ist dein Geheimnis für ein glückliches Leben?",
    "Wie bleibst du immer so gelassen?",
    "Was ist dein größtes Talent?"
]

# Funktion zum Chatten mit dem Bot
def chat_with_bot():
    user_input = user_entry.get()
    if user_input.lower() == 'exit':
        root.quit()
    else:
        if random.choice([True, False]):
            response = random.choice(komplimente)
        else:
            response = random.choice(fragen)
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        chat_window.insert(tk.END, "Bot: " + response + "\n")
        chat_window.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

# GUI erstellen
root = tk.Tk()
root.title("KomplimentBot")

# Bild der Figur laden und skalieren
image = Image.open("figur.png")
image = image.resize((150, 150), Image.LANCZOS)  # Skalieren Sie das Bild auf 150x150 Pixel
photo = ImageTk.PhotoImage(image)

# Label für das Bild der Figur
image_label = tk.Label(root, image=photo)
image_label.pack(padx=10, pady=10)

chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_entry = tk.Entry(root, width=100)
user_entry.pack(padx=10, pady=10, fill=tk.X)
user_entry.bind("<Return>", lambda event: chat_with_bot())

send_button = tk.Button(root, text="Send", command=chat_with_bot)
send_button.pack(padx=10, pady=10)

root.mainloop()