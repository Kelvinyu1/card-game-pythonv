import tkinter as tk 
from Player import Player
from Cards import Cards
import os
import random 
from PIL import ImageTk, Image

name =""
cash =0
def open_new_screen():
    for widget in window.winfo_children():
        widget.destroy()
    
    name_label = tk.Label(text="Name")
    entry_name = tk.Entry()
    money_label = tk.Label(text="Cash amount")
    entry_money = tk.Entry()
    name_label.pack()
    entry_name.pack()
    money_label.pack()
    entry_money.pack()
    
    def display_name_cash():
        global name, cash
        name = entry_name.get()
        cash = entry_money.get()
        start_game(deck)
    
    button2 = tk.Button(text="Continue?", command=display_name_cash)
    button2.pack()





window = tk.Tk()
window.geometry("800x800")
welcome_message = tk.Label(
    text="Simple Card Game made by me",
    fg="white",
    bg="green",
    width=40,
    height =20
)
welcome_message.pack()

button = tk.Button(
    text="Click me to start",
    width = 15,
    height = 10,
    fg="white",
    bg="blue",
    command=open_new_screen
)
button.pack()

current_dir = os.getcwd()
sub_dir = "cardimg"

pathing = os.path.join(current_dir, sub_dir)

deck = []
suits = ['diamonds', 'clubs', 'hearts', 'spades']
denoms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
i = 1

for suit in suits: 
    for denom in denoms:
        img_name = f"{denom}_of_{suit}.png"
        img_path = os.path.join(pathing, img_name)
        deck.append(Cards(suit, denom, i, img_path))
        i+=1

def start_game(deck):
    for widget in window.winfo_children():
        widget.destroy()
    n = tk.Label(text=name, width=15)
    c = tk.Label(text=cash, width=15)
    n.pack()
    c.pack()
    frame = tk.Frame(window)
    frame.pack()

    random_list = random.sample(range(1, 53), 5)


    #display the field 
    field = []

    for i in range(len(random_list)):
        index = random_list[i]
        field.append(deck[index])

    for i in range(0,3):
        img = field[i].get_img()
        resized_img = img.resize((100,150))

        card_img = ImageTk.PhotoImage(resized_img)
        card_label = tk.Label(frame, image=card_img)

        card_label.image = card_img

        card_label.pack(side="left")
    
    frame1 = tk.Frame(window)
    frame1.pack()

    random_hand = random.sample(range(1,53), 2)
    phand = []
    pindex = random_hand[0]
    pindex1 = random_hand[1]
    phand.append(deck[pindex])
    phand.append(deck[pindex1])

    player = Player(name, cash, phand)

    for card in phand:
        img = card.get_img()
        resized_img = img.resize((100,150))

        card_img = ImageTk.PhotoImage(resized_img)
        card_label = tk.Label(frame1, image=card_img)

        card_label.image = card_img

        card_label.pack(side="left")

    def raiseplayer():
        cashraise = tk.Label("Enter amount to raise: ")
        cashraise.pack()
        
        global get_cash
        get_cash = tk.Entry()
        get_cash.pack()

        player.cash = get_cash

        c.config(text=get_cash)

    def callplayer():
        next_card = field[3].get_img()
        resizedimg = next_card.resize((100,150))

        nextc = ImageTk.PhotoImage(resizedimg)
        cardlabel = tk.Label(frame, image=nextc)

        cardlabel.image = nextc

        cardlabel.pack(side="left")
    
    

   

    
        



    
    

    


















window.mainloop()