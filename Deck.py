__author__ = 'Jessy'


import random

RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

SUITS = ('Heart', 'Diamonds', 'Club', 'Spades')





class Card:




# Create a card with suit and rank information
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank = rank


    def __str__(self):
        return self.suit+" "+str(self.rank)


    def getSuit(self):
        return self.suit


    def getRank(self):
        return self.rank



class Deck:


    # Create a deck of cards

    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))



# Shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)



#   deal two cards
    def draw_two(self):

        card1 = random.choice(self.cards)
        card2 = random.choice(self.cards)
        hand = []
        hand.append(card1)
        hand.append(card2)
        return hand


#  deal one card
    def draw_one(self):

        card = random.choice(self.cards)

        return card



    def __str__(self):
        result = " "
        for card in self.cards:
            result += " "+card.__str__()

        return "Deck has cards of " + result