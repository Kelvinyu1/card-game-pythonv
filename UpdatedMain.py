import tkinter as tk 
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


    for card in phand:
        img = card.get_img()
        resized_img = img.resize((100,150))

        card_img = ImageTk.PhotoImage(resized_img)
        card_label = tk.Label(frame1, image=card_img)

        card_label.image = card_img

        card_label.pack(side="left")

    def raiseplayer():
        frame3 = tk.Frame(window)
        frame3.pack()

        cashraise = tk.Label(frame3, text="Enter amount: ")
        cashraise.pack()
        
        global get_cash
        get_cash = tk.Entry(frame3)
        
        get_cash.pack()
        

        def con():
            new_cash = int(get_cash.get())
            intcash = int(cash)

            global cc
            cc  = intcash - new_cash
            c.config(text=str(cc))

            next_card = field[3].get_img()
            resizedimg = next_card.resize((100,150))

            nextc = ImageTk.PhotoImage(resizedimg)
            cardlabel = tk.Label(frame, image=nextc)

            cardlabel.image = nextc

            cardlabel.pack(side="left")
            Raise.destroy()
            Call.destroy()
            get_cash.destroy()
            cashraise.destroy()
            buttonagain.destroy()
            create()
            

        buttonagain = tk.Button( text="enter", command = con)
        buttonagain.pack()


    def callplayer():
        next_card = field[3].get_img()
        resizedimg = next_card.resize((100,150))

        nextc = ImageTk.PhotoImage(resizedimg)
        cardlabel = tk.Label(frame, image=nextc)

        cardlabel.image = nextc

        cardlabel.pack(side="left")
        Call.destroy()
        Raise.destroy()
        create()
    
    Call  = tk.Button(text="Call", command=callplayer)
    Call.pack()

    Raise = tk.Button(text="Raise" ,command=raiseplayer)
    Raise.pack()


    def callcall():
        next_card = field[4].get_img()
        resizedimg = next_card.resize((100,150))

        nextc = ImageTk.PhotoImage(resizedimg)
        cardlabel = tk.Label(frame, image=nextc)

        cardlabel.image = nextc

        cardlabel.pack(side="left")
        Call2.destroy()
        Raise2.destroy()
    
    def raiseraise():
        frame3 = tk.Frame(window)
        frame3.pack()

        cashraise = tk.Label(frame3, text="Enter amount: ")
        cashraise.pack()
        
        global get_cash
        get_cash = tk.Entry(frame3)
        
        get_cash.pack()
        

        def con():
            new_cash = int(get_cash.get())
            intcash = int(cash)

            cc  = intcash - new_cash
            c.config(text=str(cc))

            next_card = field[3].get_img()
            resizedimg = next_card.resize((100,150))

            nextc = ImageTk.PhotoImage(resizedimg)
            cardlabel = tk.Label(frame, image=nextc)

            cardlabel.image = nextc

            cardlabel.pack(side="left")
            Raise2.destroy()
            Call2.destroy()
            get_cash.destroy()
            get_cash.destroy()
            buttonagain.destroy()
            cashraise.destroy()

        buttonagain = tk.Button( text="enter", command = con)
        buttonagain.pack()
    

    
    def create():
        global Call2, Raise2
        Call2 =tk.Button(text="Call", command=callcall)
        Call2.pack()

        Raise2 = tk.Button(text="Raise", command=raiseraise)
        Raise2.pack()

    def hasFlush():
        firstSuit = all_cards[0].suit

        for i  in range(1, len(all_cards)):
            if all_cards[i].suit != firstSuit:
                return False
        return True

    def check():
        doublesCount = 0
        triplesCount = 0
        hasFullHouse = False
        doublePairsCount = 0
        hasFourofAKind = False
        hasStraight = False

        global all_cards
        all_cards = []
        for i in range(0,5):
            all_cards.append(field[i])
        all_cards.append(phand[0])
        all_cards.append(phand[1])

       
        for i in range(len(all_cards)):
            sameTypeCount = 1
            card1 = all_cards[i]
            for j in range(i+1, len(all_cards)):
                card2 = all_cards[j]
                type1 = card1.denom
                type2 = card2.denom
                
                if type1 == type2:
                    sameTypeCount+=1
        
            if sameTypeCount ==2:
                doublesCount+=1
            elif sameTypeCount ==3:
                triplesCount+=1
            elif sameTypeCount ==4:
                hasFourofAKind = True
        
        if triplesCount>=1 and doublesCount>=1:
            hasFullHouse = True
        if doublesCount>=2:
            doublePairsCount = doublesCount/2

        value_list = []
        for cards in all_cards:
            value = cards.value
            value_list.append(value)
        
        value_list.sort()

        if len(value_list) >=5:
            for i in range (len(value_list)-5):
                if value_list[i+4] - value_list[i] ==4:
                    hasStraight = True
                    break

        flush = hasFlush()

        print("Number of doubles: {count}".format(count=doublesCount))
        print("Number of triples: {count}".format(count=triplesCount))
        print("Has Full House: {bool}".format(bool=hasFullHouse))
        print("Number of Double Pairs: {count}".format(count=doublePairsCount))
        print("Has Four of  a Kind: {bool}".format(bool=hasFourofAKind))
        print("Has Straight: {bool}".format(bool=hasStraight))
        print("Has Flush: {bool}".format(bool=flush))
        index = 0
        if doublesCount==0 and triplesCount==0 and hasFullHouse==False and doublePairsCount==0 and hasFourofAKind==False and flush==False:
            print("Has High Card: true")
            max = 0
            for i in range(len(all_cards)):
                if all_cards[i].value > max:
                    max = all_cards[i].value
                    index = i

        print("**************************\n your high card: {card}".format(card=all_cards[index].cardname()))



    result_button = tk.Button(text="get result", command=check)
    result_button.pack()



    
    
    

   

    
        



    
    

    


















window.mainloop()