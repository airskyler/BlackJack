__author__ = 'Jessy'


## Lab 3, Part 3

##    I got some help from my classmate Boyd for this problem


##   import unittest class to test method in the testDeck class,
#    testPlayer class and testDealer class

import unittest


##  from Deck file, import Deck class and Card class
##  from BlackJack file, import Player class, Dealer class and playGame class
from Deck import Deck, Card
from BlackJack import Player
from BlackJack import Dealer
from BlackJack import playGame



class testDeck(unittest.TestCase):


##   testing to see if the "draw_two" method fom the Deck class
#  is really drawing a two card by applying the value of number 2
    def test_drawTwo(self):
        hand = Deck().draw_two()
        self.assertEqual(len(hand),2,"There are two cards in hand")




##   testing to see if the "draw_one" method fom the Deck class
#  is really drawing a one card
    def test_drawOne(self):
        hand = Deck().draw_one()
        self.assertEqual(type(hand),Card,"There is one card in hand")



## class to test the player point
class testPlayer(unittest.TestCase):


#  testing to see if the giving two card will give a correct sum player point.
#  testing if the Player class, sumPoint method is working correctly by applying and comparing the number 9 for equality

    def test_sumPoint(self):
        playerCard = [Card("Heart",7),Card("Diamond", 2)]  #   give a two random card value to test
        playerJ = Player(playerCard)
        self.assertEqual(playerJ.sumPoint(),9,"The sum point of card is correct")




#  testing to see if the giving two card will give a correct sum player point.
#  testing if the Player class, sumPoint method is working correctly by applying and comparing the number 21 for equality

    def test_sumPointBJ(self):
        playerCard = [Card("Heart",1),Card("Diamond", 10)]
        playerJ = Player(playerCard)
        self.assertEqual(playerJ.sumPoint(),21,"The sum point of card is BlackJack")




#  testing to see if the giving two card will give a correct sum player point.
#  testing if the Player class, sumPoint method is working correctly by applying and comparing the number 20 for equality

    def test_sumPointA(self):
        playerCard = [Card("Heart",13),Card("Diamond", 13)]
        playerJ = Player(playerCard)
        self.assertEqual(playerJ.sumPoint(),20,"The sum point of card is twenty ")




#  class to test dealer point
class testDealer(unittest.TestCase):


#  testing to see if the giving two card will give a correct sum dealer point.
#  testing if the Dealer class, sumPointD method is working correctly by applying and comparing the number 9 for equality

    def test_sumPoint(self):
        dealerCard = [Card("Heart",7),Card("Diamond", 2)]
        dealerJ = Dealer(dealerCard)
        self.assertEqual(dealerJ.sumPointD(),9,"The sum point of card is correct")




#  testing to see if the giving two card will give a correct sum dealer point.
#  testing if the Dealer class, sumPointD method is working correctly by applying and comparing the number 21 for equality

    def test_sumPointBJ(self):
        dealerCard = [Card("Heart",1),Card("Diamond", 10)]
        dealerJ = Dealer(dealerCard)
        self.assertEqual(dealerJ.sumPointD(),21,"The sum point of card is BlackJack")




#  testing to see if the giving two card will give a correct sum dealer point.
#  testing if the Dealer class, sumPointD method is working correctly by applying and comparing the number 20 for equality

    def test_sumPointA(self):
        dealerCard = [Card("Heart",13),Card("Diamond", 13)]
        dealerJ = Dealer(dealerCard)
        self.assertEqual(dealerJ.sumPointD(),20,"The sum point of card is twenty ")




#  class to test the final player point and dealer point
class testComparePoint(unittest.TestCase):

    def test_comparePointDwin(self):
        pointObject = playGame()
        pointObject.dPoint = 12  ## I am directly assigning a points for the dealer and player to test
        pointObject.pPoint = 7

#  calling the comparePoint method in the playGame class to compare assigned player and dealer point
        pointObject.comparePoint()

        ##   testing to see, if the dealer win count valued turned to one, because, dealer won the game
        self.assertEqual(pointObject.dWin,1,"The dealer win count is working")




    def test_comparePointPwin(self):
        pointObject = playGame()
        pointObject.dPoint = 12  ## I am directly assigning a points for the dealer and player to test
        pointObject.pPoint = 16


        pointObject.comparePoint()

        ##   testing to see, if the player win count valued turned to one, because, player won the game
        self.assertEqual(pointObject.pWin,1,"The player win count is working")



    def test_comparePointTie(self):
        pointObject = playGame()
        pointObject.dPoint = 16  ## I am directly assigning a points for the dealer and player to test
        pointObject.pPoint = 16


        pointObject.comparePoint()

        ##   testing to see, if the tie count valued turned to one, because, dealer and player tie the game
        self.assertEqual(pointObject.tie,1,"The tie count is working")










