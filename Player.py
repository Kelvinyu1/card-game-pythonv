class Player:
    def __init__(self, name, cash, hand):
        self.name= name
        self.cash = cash
        self.hand = hand 
    
    def __str__(self):
        return "{}: \ncash: {}".format(self.name, self.cash)

    def gethand(self, index):
        card = self.hand[index]
        return card

