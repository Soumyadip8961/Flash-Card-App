BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import csv
fr_en={}
dict={}
flip=None
#-------------------------------------------Flip Card----------------------------------------------#
def flip_card():
    global fr_en
    canvas.itemconfig(image, image=img_back,  )
    canvas.itemconfig(title, text='English', fill="white")
    canvas.itemconfig(word, text=fr_en["English"], fill="white")





#--------------------------------------------Access CSV File---------------------------------------#
try:
    data=pandas.read_csv("words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    dict = original_data.to_dict(orient="records")

else:
    dict = data.to_dict(orient="records")

def known_so_next_card():
    unknown()
    dict.remove(fr_en)
    words_to_learn=pandas.DataFrame(dict)
    words_to_learn.to_csv("words_to_learn.csv", index=False)



def unknown():
    global fr_en, flip
    window.after_cancel(flip)
    fr_en = random.choice(dict)
    canvas.itemconfig(title, text='French', fill="black")
    canvas.itemconfig(word, text=fr_en["French"], fill="black")
    canvas.itemconfig(image, image=img)
    flip = window.after(3000, flip_card)



#--------------------------------------------UI SETUP-----------------------------------------------#
window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip=window.after(3000, flip_card)


canvas=Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
img=PhotoImage(file="../Flash Card Project/images/card_front.png")
img_back=PhotoImage(file="images/card_back.png")
image=canvas.create_image(400, 263, image=img )
title=canvas.create_text(400,150, text="Title", font=("normal", 20, "italic"))
word=canvas.create_text(400,250, text="Word", font=("courier", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_img=PhotoImage(file="../Flash Card Project/images/wrong.png")
cross_btn=Button(image=cross_img, highlightthickness=0, borderwidth=0, command=unknown)
cross_btn.grid(column=0, row=1)

right_img=PhotoImage(file="../Flash Card Project/images/right.png")
right_btn=Button(image=right_img, highlightthickness=0, borderwidth=0, command=known_so_next_card)
right_btn.grid(column=1, row=1)


known_so_next_card()


window.mainloop()