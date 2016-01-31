


#    Project 1
#    For this project, I got some help building the code by looking at some other people's
#    work online to start this project.  But, I basically did write these code my self.
#    some of the code reference url is

#    https://github.com/AndreDegel/blackjack/blob/master/blackjack.py
#    http://codereview.stackexchange.com/questions/57849/blackjack-game-with-classes-instead-of-functions


##   Hi, Ms. Clare James.

##   So...  I have made many changed to this project 1 code. I have added the method called "humanPlay"
##   to keep track the human player side of the input and  player point

##   I have also added a method called "dealer" to keep track the dealer side of the card and dealer point

##   I have also added a method called " comparePoint" to compare the final player point and dealer point for to
##   check who won the game or tied the game

##   I have also added a global variable for the player point called "self.pPoint" and dealer point called
##   "self.dPoint" in side the playGame class.
#    (this made me so much easier to keep track the point for player and dealer and I was able to complete the
#    Blackjack code myself)




from Deck import Deck




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

        self.dWin = 0

        self.pWin = 0

        self.tie = 0

        self.dPoint = 0   ## variable to keep track the player point and dealer point
        self.pPoint = 0



    def getTie(self):

        return self.tie


    def getDwin(self):

        return self.dWin


    def getPwin(self):

        return self.pWin




    def bjGame(self):



        #   deal two random cards to dealer and player
        self.pCards = Player(self.cards.draw_two())
        self.dCards = Dealer(self.cards.draw_two())



        self.pPoint = self.pCards.sumPoint()
        print("Player's Card:\n" +str(self.pCards) +"\n"+ "  Point: " + str(self.pPoint)+"\n")


        self.dPoint = self.dCards.sumPointD()
        print("Dealer's Card:\n" +str(self.dCards) +"\n"+ "  Point: " + str(self.dPoint)+"\n")





##   human decide to hit the card or not and add

    def humanPlay(self):

        while True:

            self.dPoint = self.dCards.sumPointD()
#   first, get player's card and sum of point
            if self.pCards.sumPoint() <= 21:
                pAnswer = input("Player... Do you want a new card? Please Type Capital letter [ Y or N ]\n")

                if pAnswer == "Y":
                    self.pCards.pAdd_card(self.cards.draw_one())
                    self.pPoint= self.pCards.sumPoint()
                    print("Player's card :\n "+str(self.pCards) +"\n" + "   Point: " + str(self.pPoint)+"\n")

                    if self.pPoint > 21:
                        return self.pPoint
                        break




                elif pAnswer == "N":
                    self.pPoint = self.pCards.sumPoint()

                    print("Player's final card :\n "+str(self.pCards) +"\n" + "   Point: " + str(self.pPoint)+"\n")


                    print("Dealer's Card:\n" +str(self.dCards) +"\n"+ "  Point: " + str(self.dPoint)+"\n")

                    return self.pPoint
                    break


            elif self.pPoint > 21:
                return self.pPoint
                break





#    if, dealer's card point is lower than 17... dealer hits the card till the point is over 17.
#   after getting the player and dealer's card point, compare the point and write the result in a file
    def dealer(self):

        while True:

            if self.dPoint < 17 and self.pPoint <= 21:
                self.dCards.dAdd_card(self.cards.draw_one())
                self.dPoint = self.dCards.sumPointD()
                print("Dealer's card :\n " +str(self.dCards)+"\n"+ "   Point: "+str(self.dPoint)+"\n")


                if self.dPoint >= 17:
                    return self.dPoint
                    break


            else:
                return self.dPoint
                break






##  Comparing the total human point and total dealer point

    def comparePoint(self):



        if self.dPoint == self.pPoint:
            print("P: "+str(self.pPoint)+ "   D: "+str(self.dPoint))
            print("It is a tie")
            self.tie = self.tie + 1



        elif (self.dPoint <= 21 and self.pPoint <= 21) and self.dPoint > self.pPoint:
            print("P: "+str(self.pPoint)+ "   D: "+str(self.dPoint))
            print("Dealer win")
            self.dWin = self.dWin + 1




        elif (self.dPoint <= 21 and self.pPoint <= 21) and self.dPoint < self.pPoint:
            print("P: "+str(self.pPoint)+ "   D: "+str(self.dPoint))
            print("Player win")
            self.pWin = self.pWin + 1



        elif self.pPoint > 21 and self.dPoint <= 21:
            print("P: "+str(self.pPoint)+ "   D: "+str(self.dPoint))
            print("Player lose, Dealer win  \n")
            self.dWin = self.dWin + 1



        elif self.pPoint == 21 and self.dPoint < 21:
            print("P: "+str(self.pPoint)+ "   D: "+str(self.dPoint))
            print("Player win")
            self.pWin = self.pWin + 1




        elif self.dPoint > 21 and self.pPoint <= 21:
            print("P: "+str(self.pPoint)+ "   D: "+str(self.dPoint))
            print("Dealer lose, player win")
            self.pWin = self.pWin + 1







## Start the game

if __name__=='__main__':


    bj = playGame()
    def main():

        while True:
            playOrNot = input("Would you like to play Blackjack? Please type capital letter [ Y or N ]"+"\n")
            if playOrNot == "Y":
                bj.bjGame()

                bj.humanPlay()      ## get final player point
                bj.dealer()         ## get final dealer point
                bj.comparePoint()   ## compare final player point and dealer point
                                    ## and check who the winner is or tie


##  if the user decide to not play the game anymore, display the game result

            else:
                print("Game finished")

                strT = 'Tie count is:  '
                strD = 'Dealer win count is:  '
                strP = 'Player win count is:  '


                f = open('Winner Count', 'w')    ##  open writable file

                try:
                    f = open("Winner ")

                except IOError:
                    print("This file doesn't exist!... This is just a test print sentence \n")
                    pass


                f = open('Winner Count', 'w')

                print("The game result is :")

                f.write(strT + str(bj.getTie())+"\n")
                f.write(strD + str(bj.getDwin())+"\n")
                f.write(strP + str(bj.getPwin())+"\n")

                f.close()


                f = open('Winner Count', 'r')   ## read the result of the winner count and tie count
                                                #  of the game from file and display it
                for line in f:
                    print(line)
                f.close()


                break


    main()












