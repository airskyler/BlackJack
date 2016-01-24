


#    Project 1 -  By Jessy Mullen

#    For this project, I got some help building the code by looking at some other people's
#    work online to start this project.  But, I basically did write these code my self.

#    some of the code reference url is

#    https://github.com/AndreDegel/blackjack/blob/master/blackjack.py
#    http://codereview.stackexchange.com/questions/57849/blackjack-game-with-classes-instead-of-functions

#    Some stuff I need to work on is... I need to have a Card class and Deck class separately, I was trying to create
#    a new class but, I couldn't figure out. I also should just use one counting function rather than two counting
#    function.  I also need to work on counting the total wins and ties for the writing and reading file




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




class Player:

    def __init__(self, cards):
        self.player_Hand = cards


    def __str__ (self):
        pResult = " "
        for card in self.player_Hand:
            pResult += " "+card.__str__()

        return pResult


    def pAdd_card(self, card):
        self.player_Hand.append(card)


#  Counting point function
    def sumPoint(self):
        point = 0

        for card in self.player_Hand:
            if card.rank > 9:
                point += 10

            elif card.rank == 1:
                point += 11

            else:
                point += card.rank   # adding 1 to 9 points

        for card in self.player_Hand:
            if point <= 21:
                break

            elif card.rank == 1:
                point -= 10

        return point





class Dealer:


    def __init__(self, cards):
        self.dealer_Hand = cards


    def __str__ (self):
        dResult = " "
        for card in self.dealer_Hand:
            dResult += " "+card.__str__()

        return dResult


    def dAdd_card(self, card):
        self.dealer_Hand.append(card)




#  Counting points function
    def sumPointD(self):
        point = 0

        for card in self.dealer_Hand:
            if card.rank > 9:
                point += 10

            elif card.rank == 1:
                point += 11

            else:
                point += card.rank   # adding 1 to 9 points

        for card in self.dealer_Hand:
            if point <= 21:
                break

            elif card.rank == 1:
                point -= 10

        return point




class playGame(object):

    def __init__(self):

        self.cards = Deck()
        self.cards.shuffle()

#   deal two random cards to dealer and player
        self.pCards = Player(self.cards.draw_two())
        self.dCards = Dealer(self.cards.draw_two())


    def bjGame(self):

        dWin = 0

        pWin = 0

        tie = 0

        strT = 'Tie count is:  '
        strD = 'Dealer win count is:  '
        strP = 'Player win count is:  '


        f = open('Winner Count', 'a')


        pPoint = self.pCards.sumPoint()
        print("Player's Card:\n" +str(self.pCards) +"\n"+ "  Point: " + str(pPoint)+"\n")


        dPoint = self.dCards.sumPointD()
        print("Dealer's Card:\n" +str(self.dCards) +"\n"+ "  Point: " + str(dPoint)+"\n")





        while True:

#   first, get player's card and sum of point
            if pPoint <= 21:
                pAnswer = input("Player... Do you want a new card? Please Type Capital letter [ Y or N ]\n")

                if pAnswer == "Y":
                    self.pCards.pAdd_card(self.cards.draw_one())
                    pPoint = self.pCards.sumPoint()
                    print("Player's card :\n "+str(self.pCards) +"\n" + "   Point: " + str(pPoint)+"\n")

                    if pPoint > 21:
                        break



                elif pAnswer == "N":
                    pPoint = self.pCards.sumPoint()
                    print("Player's final card :\n "+str(self.pCards) +"\n" + "   Point: " + str(pPoint)+"\n")


                    print("Dealer's Card:\n" +str(self.dCards) +"\n"+ "  Point: " + str(dPoint)+"\n")
                    break



        if pPoint <= 21 and (dPoint <= 21 and dPoint >= 17)and dPoint == pPoint:

            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("It is a tie")
            tie = tie + 1
            f.write(strT + str(tie)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()





        elif pPoint > 21:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Player lose  \n")
            dWin = dWin + 1
            f.write(strD + str(dWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()






        elif pPoint <= 21 and (dPoint <= 21 and dPoint >= 17) and dPoint > pPoint:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Dealer win")
            dWin = dWin + 1
            f.write(strD + str(dWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()





        elif pPoint <= 21 and (dPoint <= 21 and dPoint >= 17)and pPoint > dPoint:

            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Player win")
            pWin = pWin + 1
            f.write(strP + str(pWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()






#    if, dealer's card point is lower than 17... dealer hits the card till the point is over 17.
#   after getting the player and dealer's card point, compare the point and write the result in a file


        while True:
            if dPoint < 17 and pPoint <= 21:
                self.dCards.dAdd_card(self.cards.draw_one())
                dPoint = self.dCards.sumPointD()
                print("Dealer's card :\n " +str(self.dCards)+"\n"+ "   Point: "+str(dPoint)+"\n")


                if dPoint > 17:
                    break


        if dPoint == pPoint:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("It is a tie")
            tie = tie + 1
            f.write(strT + str(tie)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()



        elif (dPoint <= 21 and pPoint <= 21) and dPoint > pPoint:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Dealer win")
            dWin = dWin + 1
            f.write(strD + str(dWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()




        elif (dPoint <= 21 and pPoint <= 21) and dPoint < pPoint:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Dealer win")
            dWin = dWin + 1
            f.write(strD + str(dWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()





        elif pPoint > 21 and dPoint <= 21:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Player lose, Dealer win  \n")
            dWin = dWin + 1
            f.write(strD + str(dWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()




        elif pPoint == 21 and dPoint < 21:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Player win")
            pWin = pWin + 1
            f.write(strP + str(pWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()




        elif dPoint > 21 and pPoint <= 21:
            print("P: "+str(pPoint)+ "   D: "+str(dPoint))
            print("Dealer lose, player win")
            pWin = pWin + 1
            f.write(strP + str(pWin)+"\n")
            f.close()

            f = open('Winner Count', 'r')
            for line in f:
                print(line)
            f.close()





#   Start the game by asking the user... if the user want to play blackjack

bj = playGame()
def main():

    playOrNot = input("Would you like to play Blackjack? Please type capital letter [ Y or N ]"+"\n")
    if playOrNot == "Y":
        bj.bjGame()

    else:
        print("Game finished")


main()












