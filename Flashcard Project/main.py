import random
from tkinter import *
import pandas as pd
import csv

BACKGROUND_COLOR = "#B1DDC6"

title = ("Ariel", 40, "italic")
words = ("Ariel", 60, "bold")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    file = open("data/french_words.csv","r")
except FileNotFoundError as f:
    print(f"No such file as {f} found")
else:
    datas = pd.read_csv("data/french_words.csv")
    french = datas.French.to_list()
    english = datas.English.to_list()

finally:
    file.close()

print(french)
print(english)

fw = ""
ew = ""

def random_word():
    global fw,ew
    fw = random.choice(french)
    ew = random.choice(english)
    return [fw,ew]

def next_word():
    random_word()
    global fw,ew
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_text,text= "French")
    canvas.itemconfig(card_word, text=fw)

    canvas.after(2000,func=flip_card)
    english.remove(french[fw])
    french.remove(french[ew])

def flip_card():
    canvas.itemconfig(canvas_image, image = card_front_image)
    canvas.itemconfig(card_text, text="English", font=title)
    canvas.itemconfig(card_word, text=english[french.index(fw)])



def dont_know():

    global fw, ew
    # Append the unknown word to a CSV file
    with open("unknown_word.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([fw, english[french.index(fw)]])
    random_word()
    # Update the canvas to show the back of the card and the French word
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_text, text="French")
    canvas.itemconfig(card_word, text=fw)

    # Flip the card back after 2000 ms (2 seconds)
    canvas.after(2000, func=flip_card)


card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_back_image)
card_text = canvas.create_text(400, 150, text="FLASHY", font=title)
card_word = canvas.create_text(400, 263, text="CARD", font=words)
canvas.grid(row=0, column=0, columnspan=2)
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)
right_button.config(command=next_word)
wrong_button.grid(row=1, column=0)
wrong_button.config(command=dont_know)

window.mainloop()
