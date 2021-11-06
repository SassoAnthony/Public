#Cinch
#By Anthony Sasso
#Started 10/25/19
#Completed 12/6/19

import random
import pdb
import time

def giveInstructions():
    #Prints Instructions on how to play the game
    
    print("Press the Enter key after reading each section of instructions to ")
    print("show the next section.")
    input()
    print("Welcome to Cinch.py! Cinch.py is the computer version of the not ")
    print("very popular card game known as Cinch. It is an old German card ")
    print("game, with some relatively complicated rules, so please read carefully.")
    input()
    print("This game is played in teams of two, the player across from you will ")
    print("be your partner. The goal is to be the first team to have 52 points.")
    input()
    print("Each player is dealt 9 cards. Then each player will bid how many points ")
    print("they think their team can get that hand. Bidding goes clockwise, ")
    print("starting with the player to the left of hte dealer. You will deal first.")
    input()
    print("Some cards are worth points, while others are not. The A, J, 10, and 2 ")
    print("of the 'on suit' are each worth 1 point. The 5 of the 'on suit' is ")
    print("worth 5 points, and the 5 of the 'off suit' is worth 5 points.")
    input()
    print("Whoever bids the highest will get to choose what the 'on suit' will be, ")
    print("and the 'off suit' will be the other suit of the same color. (If Hearts ")
    print("is the 'on suit', then Diamonds is the 'off suit')")
    input()
    print("After the bidding process is complete and an 'on suit' is chosen, ")
    print("every card that is not the 'on suit' (or a 5 of the 'off suit') ")
    print("will be removed from your hand, and you will be dealt more cards ")
    print("until you have 6 cards.")
    input()
    print("Then the hand will begin. Each had will have 6 'tricks'. During each ")
    print("'trick', each player will play one card. Then, the player who played the ")
    print("winning card will get all of the points in the 'trick' for their team.")
    input()
    print("There is a system to decide which card wins. All cards of the 'on suit' ")
    print("win over other cards, and they beat each other in the standard order using ")
    print("the A as the high card. The 5 of the 'off suit' beats the 4, 3 and 2 of the 'on suit'.")
    input()
    print("If the first card played is and 'on suit' (or a 5 of the 'off suit'), and you have ")
    print("a card of the 'on suit'(or a 5 of the 'off suit') you must play that card.")
    input()
    print("The bidder plays first on the first 'trick', and play goes clockwise. Whoever ")
    print("won the previous 'trick' will play first after that.")
    input()
    print("After all 6 'tricks', if the team who bid did not get as many points as they bid, ")
    print("their score will go down by the amount they bid. If they did get enough points, ")
    print("then the points from the 'trick' will be awarded normally.")
    input()
    print("The score is kept using the terms 'we' and 'they'. Don't ask why, I don't know. ")
    print("All you have to know is that your team is 'we', and 'they' is the enemy.")
    input()
    print("And that's all the instructions. If you get confused or forget something, feel ")
    print("free to scroll back up here and re-read this. Or you can just keep playing. ")
    print("The code won't let you break the rules anyway. (At least I hope)")
    input()
    print("Press enter to play.")
    input()

class Card:
    #A class that stores a card's value and suit
    
    def __init__ (self, v, s):
        self.value = v
        self.suit = s

def createDeck():
    #This function creates a deck of 52 Card objects and saves them to a list

    deck = []
    cardList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suitList = ["Hearts", "Clubs", "Diamonds", "Spades"]
    for value in cardList:
        for suit in suitList:
            deck.append(Card(value, suit))
    return deck

def printCards(cards):
    #This function prints a list of cards, and was used mostly for testing purposes

    cards = sortCards(cards)

    print()
    for card in cards:
        print(card.value + card.suit + " ", end = "")
    print()

def sortCards(cards):
    #Sorts the cards by suit and value
    
    cards = sorted(cards, key = lambda card: card.value, reverse = True)
    cards = sorted(cards, key = lambda card: card.suit)

    return cards

def shuffleDeck(deck):
    #This function shuffles the deck

    random.shuffle(deck)
    return deck

def dealCards(deck):
    #This function deals 9 cards to each player and returns the hands as lists

    playerHand = []
    leftHand = []
    upHand = []
    rightHand = []

    for number in range(9):
        playerHand.append(deck[-1])
        deck.pop(-1)
        leftHand.append(deck[-1])
        deck.pop(-1)
        upHand.append(deck[-1])
        deck.pop(-1)
        rightHand.append(deck[-1])
        deck.pop(-1)

    return playerHand, leftHand, upHand, rightHand, deck

def reset():
    #This function calls functions to reset the deck and the hands
    #This function performs the operations that need to occur between rounds

    deck = createDeck()

    deck = shuffleDeck(deck)

    return dealCards(deck)

def printScreen(pHand, lHand, uHand, rHand, pCardPlayed, lCardPlayed, uCardPlayed, rCardPlayed):
    #Shows the main screen of the game
    #This function is adaptive to center different numbers of cards for each hand
    #Also it's 391 lines of code

    ##L1     _________________________________________________________________________
    ##L2    |                  |?  |?  |?  |?  |?  |?  |?  |?  |?  |                  |
    ##L3    |                  |   |   |   |   |   |   |   |   |   |                  |
    ##L4    |                  |   |   |   |   |   |   |   |   |   |                  |
    ##L5    |                  |___|___|___|___|___|___|___|___|___|                  |
    ##L6    |                                                                         |
    ##L7    |_______                                                           _______|
    ##L8    |      ?|                                                         |?      |
    ##L9    |_______|                                                         |_______|
    ##L10   |      ?|                           ___                           |?      |
    ##L11   |_______|                          |V  |                          |_______|
    ##L12   |      ?|                          |S  |                          |?      |
    ##L13   |_______|                          |   |                          |_______|
    ##L14   |      ?|                          |___|                          |?      |
    ##L15   |_______|                  _______       _______                  |_______|
    ##L16   |      ?|                 |    S V|  *  |V S    |                 |?      |
    ##L17   |_______|                 |_______| ___ |_______|                 |_______|
    ##L18   |      ?|                          |V  |                          |?      |
    ##L19   |_______|                          |S  |                          |_______|
    ##L20   |      ?|                          |   |                          |?      |
    ##L21   |_______|                          |___|                          |_______|
    ##L22   |      ?|                                                         |?      |
    ##L23   |_______|                                                         |_______|
    ##L24   |      ?|                                                         |?      |
    ##L25   |_______|                                                         |_______|
    ##L26   |                                                                         |
    ##L27   |                   ___ ___ ___ ___ ___ ___ ___ ___ ___                   |
    ##L28   |                  |A  |K  |Q  |10 |2  |J  |3  |6  |8  |                  |
    ##L29   |                  |H  |H  |H  |H  |H  |S  |S  |D  |C  |                  |
    ##L30   |                  |   |   |   |   |   |   |   |   |   |                  |
    ##L31   |__________________|___|___|___|___|___|___|___|___|___|__________________|

    linesPrinted = 0

    #L1 
    print(" " + "_" * 73 + " ")
    linesPrinted += 1

    #L2
    print("|" + " " * int(((73 - ((len(uHand) * 4) + 1)) / 2)), end = "")
    for card in uHand:
        print("|?  ", end = "")
    if (uHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(uHand) * 4) +1)) / 2)) + "|")
    linesPrinted += 1

    #L3
    print("|" + " " * int(((73 - ((len(uHand) * 4) + 1)) / 2)), end = "")
    for card in uHand:
        print("|   ", end = "")
    if (uHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(uHand) * 4) + 1)) / 2)) + "|")
    linesPrinted += 1

    #L4
    print("|" + " " * int(((73 - ((len(uHand) * 4) + 1)) / 2)), end = "")
    for card in uHand:
        print("|   ", end = "")
    if (uHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(uHand) * 4) + 1)) / 2)) + "|")
    linesPrinted += 1

    #L5
    print("|" + " " * int(((73 - ((len(uHand) * 4) + 1)) / 2)), end = "")
    for card in uHand:
        print("|___", end = "")
    if (uHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(uHand) * 4) + 1)) / 2)) + "|")
    linesPrinted += 1

    #L6 - Top of Side Cards
    for i in range(int(((21 - ((len(lHand) * 2) + 1)) / 2))):
        #If cards in middle
        if (uCardPlayed != None and linesPrinted == 9):
            print("|" + " " * 35 + "___" + " " * 35 + "|")
        elif (uCardPlayed != None and linesPrinted == 10):
            if (uCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|" + " " * 34 + "|" + uCardPlayed.value + " " * numSpaces + "|" + " " * 34 + "|")
        elif (uCardPlayed != None and linesPrinted == 11):
            print("|" + " " * 34 + "|" + uCardPlayed.suit[0] + " " * 2 + "|" + " " * 34 + "|")
        elif (uCardPlayed != None and linesPrinted == 12):
            print("|" + " " * 34 + "|   |" + " " * 34 + "|")
        elif (uCardPlayed != None and linesPrinted == 13):
            print("|" + " " * 34 + "|___|" + " " * 34 + "|")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 14):
            print("|" + " " * 25, end = "")
            if (lCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 5, end = "")
            if (rCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 25 + "|")
        #If no cards in middle
        else:
            print("|" + " " * 73 + "|")
        linesPrinted += 1

    #First Line of Side Cards
    #If side cards
    if (lHand != []):
        #If cards in middle
        if (uCardPlayed != None and linesPrinted == 9):
            print("|______" + " " * 29 + "___" + " " * 35 + "|")
        elif (uCardPlayed != None and linesPrinted == 10):
            if (uCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|______" + " " * 28 + "|" + uCardPlayed.value + " " * numSpaces + "|" + " " * 28 + "______|")
        elif (uCardPlayed != None and linesPrinted == 11):
            print("|______" + " " * 28 + "|" + uCardPlayed.suit[0] + " " * 2 + "|" + " " * 28 + "______|")
        elif (uCardPlayed != None and linesPrinted == 12):
            print("|______" + " " * 28 + "|   |" + " " * 28 + "______|")
        elif (uCardPlayed != None and linesPrinted == 13):
            print("|______" + " " * 28 + "|___|" + " " * 28 + "______|")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 14):
            print("|______" + " " * 19, end = "")
            if (lCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 5, end = "")
            if (rCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 19 + "______|")
            
        #If no cards in middle
        else:
            print("|______" + " " * 61 + "______|")

    #If no side cards
    else:
        print("|" + " " * 25, end = "")
        if (lCardPlayed != None and linesPrinted == 15):
            if (lCardPlayed.value == "10"):
                numSpaces = 3
            else:
                numSpaces = 4
            print("|" + " " * numSpaces + lCardPlayed.suit[0] + " " + lCardPlayed.value + "|", end = "")
        else:
            print(" " * 9, end = "")
        print(" " * 5, end = "")
        if (rCardPlayed != None and linesPrinted == 15):
            if (rCardPlayed.value == "10"):
                numSpaces = 3
            else:
                numSpaces = 4
            print("|" + rCardPlayed.value + " " + rCardPlayed.suit[0] + " " * numSpaces + "|", end = "")
        else:
            print(" " * 9, end = "")
        print(" " * 25 + "|")
    linesPrinted += 1
                  
    #Side Cards
    for card in lHand:
        #If cards in middle
        if (uCardPlayed != None and linesPrinted == 9):
            print("|     ?|" + " " * 28 + "___" + " " * 28 + "|?     |")
        elif (uCardPlayed != None and linesPrinted == 10):
            if (uCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|     ?|" + " " * 27 + "|" + uCardPlayed.value + " " * numSpaces + "|" + " " * 27 + "|?     |")
        elif (uCardPlayed != None and linesPrinted == 11):
            print("|     ?|" + " " * 27 + "|" + uCardPlayed.suit[0] + " " * 2 + "|" + " " * 27 + "|?     |")
        elif (uCardPlayed != None and linesPrinted == 12):
            print("|     ?|" + " " * 27 + "|   |" + " " * 27 + "|?     |")
        elif (uCardPlayed != None and linesPrinted == 13):
            print("|     ?|" + " " * 27 + "|___|" + " " * 27 + "|?     |")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 14):
            print("|     ?|" + " " * 18, end = "")
            if (lCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 5, end = "")
            if (rCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 18 + "|?     |")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 15):
            print("|     ?|" + " " * 18, end = "")
            if (lCardPlayed != None and linesPrinted == 15):
                if (lCardPlayed.value == "10"):
                    numSpaces = 3
                else:
                    numSpaces = 4
                print("|" + " " * numSpaces + lCardPlayed.suit[0] + " " + lCardPlayed.value + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 5, end = "")
            if (rCardPlayed != None and linesPrinted == 15):
                if (rCardPlayed.value == "10"):
                    numSpaces = 3
                else:
                    numSpaces = 4
                print("|" + rCardPlayed.value + " " + rCardPlayed.suit[0] + " " * numSpaces + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 18 + "|?     |")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 16):
            print("|     ?|" + " " * 18, end = "")
            if (lCardPlayed != None):
                print("|" + "_" * 7 + "|", end = "")
            else:
                print(" " * 9, end = "")
            if (pCardPlayed != None):
                print(" ___ ", end = "")
            else:
                print(" " * 5, end = "")
            if (rCardPlayed != None):
                print("|" + "_" * 7 + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 18 + "|?     |")
        elif (pCardPlayed != None and linesPrinted == 17):
            if (pCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|     ?|" + " " * 27 + "|" + pCardPlayed.value + " " * numSpaces + "|" + " " * 27 + "|?     |")
        elif (pCardPlayed != None and linesPrinted == 18):
            print("|     ?|" + " " * 27 + "|" + pCardPlayed.suit[0] + " " * 2 + "|" + " " * 27 + "|?     |")
        elif (pCardPlayed != None and linesPrinted == 19):
            print("|     ?|" + " " * 27 + "|   |" + " " * 27 + "|?     |")
        elif (pCardPlayed != None and linesPrinted == 20):
            print("|     ?|" + " " * 27 + "|___|" + " " * 27 + "|?     |")
            
        #If no cards in middle
        else:
            print("|     ?|" + " " * 59 + "|?     |")
        linesPrinted += 1

        #If cards in middle
        if (uCardPlayed != None and linesPrinted == 9):
            print("|______|" + " " * 28 + "___" + " " * 28 + "|______|")
        elif (uCardPlayed != None and linesPrinted == 10):
            if (uCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|______|" + " " * 27 + "|" + uCardPlayed.value + " " * numSpaces + "|" + " " * 27 + "|______|")
        elif (uCardPlayed != None and linesPrinted == 11):
            print("|______|" + " " * 27 + "|" + uCardPlayed.suit[0] + " " * 2 + "|" + " " * 27 + "|______|")
        elif (uCardPlayed != None and linesPrinted == 12):
            print("|______|" + " " * 27 + "|   |" + " " * 27 + "|______|")
        elif (uCardPlayed != None and linesPrinted == 13):
            print("|______|" + " " * 27 + "|___|" + " " * 27 + "|______|")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 14):
            print("|______|" + " " * 18, end = "")
            if (lCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 5, end = "")
            if (rCardPlayed != None):
                print(" " + "_" * 7 + " ", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 18 + "|______|")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 15):
            print("|______|" + " " * 18, end = "")
            if (lCardPlayed != None and linesPrinted == 15):
                if (lCardPlayed.value == "10"):
                    numSpaces = 3
                else:
                    numSpaces = 4
                print("|" + " " * numSpaces + lCardPlayed.suit[0] + " " + lCardPlayed.value + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 5, end = "")
            if (rCardPlayed != None and linesPrinted == 15):
                if (rCardPlayed.value == "10"):
                    numSpaces = 3
                else:
                    numSpaces = 4
                print("|" + rCardPlayed.value + " " + rCardPlayed.suit[0] + " " * numSpaces + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 18 + "|______|")
        elif ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 16):
            print("|______|" + " " * 18, end = "")
            if (lCardPlayed != None):
                print("|" + "_" * 7 + "|", end = "")
            else:
                print(" " * 9, end = "")
            if (pCardPlayed != None):
                print(" ___ ", end = "")
            else:
                print(" " * 5, end = "")
            if (rCardPlayed != None):
                print("|" + "_" * 7 + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 18 + "|______|")
        elif (pCardPlayed != None and linesPrinted == 17):
            if (pCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|______|" + " " * 27 + "|" + pCardPlayed.value + " " * numSpaces + "|" + " " * 27 + "|______|")
        elif (pCardPlayed != None and linesPrinted == 18):
            print("|______|" + " " * 27 + "|" + pCardPlayed.suit[0] + " " * 2 + "|" + " " * 27 + "|______|")
        elif (pCardPlayed != None and linesPrinted == 19):
            print("|______|" + " " * 27 + "|   |" + " " * 27 + "|______|")
        elif (pCardPlayed != None and linesPrinted == 20):
            print("|______|" + " " * 27 + "|___|" + " " * 27 + "|______|")
            
        #If no cards in middle
        else:
            print("|______|" + " " * 59 + "|______|")
        linesPrinted += 1

    #Bottom of Side Cards - L26
    for i in range(int(((21 - ((len(lHand) * 2) + 1)) / 2))):
        if ((lCardPlayed != None or rCardPlayed != None) and linesPrinted == 16):
            print("|" + " " * 25, end = "")
            if (lCardPlayed != None):
                print("|" + "_" * 7 + "|", end = "")
            else:
                print(" " * 9, end = "")
            if (pCardPlayed != None):
                print(" ___ ", end = "")
            else:
                print(" " * 5, end = "")
            if (rCardPlayed != None):
                print("|" + "_" * 7 + "|", end = "")
            else:
                print(" " * 9, end = "")
            print(" " * 25 + "|")
        elif (pCardPlayed != None and linesPrinted == 17):
            if (pCardPlayed.value == "10"):
                numSpaces = 1
            else:
                numSpaces = 2
            print("|" + " " * 34 + "|" + pCardPlayed.value + " " * numSpaces + "|" + " " * 34 + "|")
        elif (pCardPlayed != None and linesPrinted == 18):
            print("|" + " " * 34 + "|" + pCardPlayed.suit[0] + " " * 2 + "|" + " " * 34 + "|")
        elif (pCardPlayed != None and linesPrinted == 19):
            print("|" + " " * 34 + "|   |" + " " * 34 + "|")
        elif (pCardPlayed != None and linesPrinted == 20):
            print("|" + " " * 34 + "|___|" + " " * 34 + "|")
        else:
            print("|" + " " * 73 + "|")
        linesPrinted += 1

    #L27
    print("|" + " " * int(((73 - ((len(pHand) * 4) + 1)) / 2)), end = "")
    for card in pHand:
        print(" ___", end = "")
    print(" ", end = "")
    print(" " * int(((73 - ((len(pHand) * 4) + 1)) / 2)) + "|")
    linesPrinted += 1

    #L28
    print("|" + " " * int(((73 - ((len(pHand) * 4) + 1)) / 2)), end = "")
    for card in pHand:
        if (card.value == "10"):
            numSpaces = 1
        else:
            numSpaces = 2
        print("|" + card.value + " " * numSpaces, end = "")
    if (pHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(pHand) * 4) +1)) / 2)) + "|")
    linesPrinted += 1

    #L29
    print("|" + " " * int(((73 - ((len(pHand) * 4) + 1)) / 2)), end = "")
    for card in pHand:
        print("|" + card.suit[0] + "  ", end = "")
    if (pHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(pHand) * 4) +1)) / 2)) + "|")
    linesPrinted += 1

    #L30
    print("|" + " " * int(((73 - ((len(pHand) * 4) + 1)) / 2)), end = "")
    for card in pHand:
        print("|   ", end = "")
    if (pHand != []):
        print("|", end = "")
    else:
        print(" ", end = "")
    print(" " * int(((73 - ((len(pHand) * 4) + 1)) / 2)) + "|")
    linesPrinted += 1

    #L31
    print("|" + "_" * int(((73 - ((len(pHand) * 4) + 1)) / 2)), end = "")
    for card in pHand:
        print("|___", end = "")
    if (pHand != []):
        print("|", end = "")
    else:
        print("_", end = "")
    print("_" * int(((73 - ((len(pHand) * 4) + 1)) / 2)) + "|")
    linesPrinted += 1

def getDealer(dIndex):
    #This function switches the dealer, returning hwo is the dealer and the list of players
    dList = ["player", "left", "up", "right"]
    d = dList[dIndex % 4]
    return d, dList, dIndex

def getBids(d, dList, pHand, lHand, uHand, rHand):
    #This function sorts dList into the proper bidding order, and then gets the bids for each player
    #The function returns the final bid's value and suit, as well as whose bid it was
    while True:
        if (dList[0] != d):
            notD = dList.pop(0)
            dList.append(notD)
        else:
            dList.pop(0)
            dList.append(d)
            break
    finalBid = 5
    finalBidSuit = None
    bidder = None
    for person in dList:
        if (person == "player"):
            while True:
                try:
                    bid = int(input("What would you like to bid? (0 = pass)"))
                    if ((bid > 5 and bid < 15) or (bid == 0)):
                        if (bid > finalBid or bid == 0):
                            break
                        else:
                            print("You must bid higher than the previous bidders or pass.")
                    else:
                        print("You must bid between 6 and 14")
                except:
                    print("Please bid using a number.")
            if (bid > finalBid):
                finalBid = bid
                finalBidSuit = None
                bidder = person
                print("You bid", bid)
            else:
                print("You passed.")
        elif (person == "left"):
            bid, bidSuit = calculateBid(lHand)
            if (bid > finalBid):
                finalBid = bid
                finalBidSuit = bidSuit
                bidder = person
                print("Left bid", str(bid) + ".")
            else:
                print("Left passed.")
        elif (person == "up"):
            bid, bidSuit = calculateBid(uHand)
            if (bid > finalBid):
                finalBid = bid
                finalBidSuit = bidSuit
                bidder = person
                print("Up bid", str(bid) + ".")
            else:
                print("Up passed.")
        elif (person == "right"):
            bid, bidSuit = calculateBid(rHand)
            if (bid > finalBid):
                finalBid = bid
                finalBidSuit = bidSuit
                bidder = person
                print("Right bid", str(bid) + ".")
            else:
                print("Right passed.")
        else:
            print("SOMETHING BROKE IN getBids()")
        time.sleep(1)
    if (bidder == None):
        print("No bids, dealer takes it for 6.")
        bidder = dList[3]
        finalBid = 6
    return finalBid, finalBidSuit, bidder

def calculateBid(hand):
    #This function calculates a bid for the hand it is sent
    #It is used to get bids from the computer controlled players
    bid = 0
    bidSuit = None
    hearts = ["Hearts"]
    diamonds = ["Diamonds"]
    clubs = ["Clubs"]
    spades = ["Spades"]
    
    for card in hand:
        if (card.suit == "Hearts"):
            hearts.append(card.value)
        elif (card.suit == "Diamonds"):
            diamonds.append(card.value)
        elif (card.suit == "Spades"):
            spades.append(card.value)
        elif (card.suit == "Clubs"):
            clubs.append(card.value)
        else:
            print("SOMETHING BROKE IN calculateBid() PART 1")
    sortedHand = [hearts, diamonds, clubs, spades]
    for suit in sortedHand:
        tempBid = 0
        for card in suit:
            if (card == "A"):
                tempBid += 6
            elif (card == "K"):
                tempBid += 1
            elif (card == "Q"):
                tempBid += 1
            elif (card == "J"):
                tempBid += 1
            elif (card == "10"):
                tempBid += 1
            elif (card == "5" and len(suit) >= 4):
                tempBid += 3
            elif (card == "2"):
                tempBid += 1
        if (tempBid > bid and tempBid >= 6):
            bid = tempBid
            bidSuit = suit[0]

    return bid, bidSuit

def getPlayerBidSuit():
    #This function asks the player for the on suit if the player wins the bid
    while (True):
        suit = input("You won the bid! What suit do you want to play? ")
        if (suit[0].lower() == "h"):
            bidSuit = "Hearts"
            break
        elif (suit[0].lower() == "s"):
            bidSuit = "Spades"
            break
        elif (suit[0].lower() == "d"):
            bidSuit = "Diamonds"
            break
        elif (suit[0].lower() == "c"):
            bidSuit = "Clubs"
            break
        else:
            print("That isn't a suit!")
    return bidSuit

def discardExtraCards(pHand, lHand, uHand, rHand, bidSuit):
    #This function automatically discards the unnecessary cards from each hand
    if (bidSuit == "Hearts"):
        offSuit = "Diamonds"
    elif (bidSuit == "Diamonds"):
        offSuit = "Hearts"
    elif (bidSuit == "Spades"):
        offSuit = "Clubs"
    elif (bidSuit == "Clubs"):
        offSuit = "Spades"
    pHand = removeCardsOfSuit(pHand, bidSuit, offSuit)
    lHand = removeCardsOfSuit(lHand, bidSuit, offSuit)
    uHand = removeCardsOfSuit(uHand, bidSuit, offSuit)
    rHand = removeCardsOfSuit(rHand, bidSuit, offSuit)
    return pHand, lHand, uHand, rHand
        
def removeCardsOfSuit(hand, suit1, suit2):
    #This function removes cards from a hand that are not of suit1 and not a 5 of suit2
    toRemoveIndexList = []
    counter = 0
    for card in hand:
        if (card.suit != suit1):
            if (card.suit != suit2):
                toRemoveIndexList.append(counter)
            elif (card.value != "5"):
                toRemoveIndexList.append(counter)
        counter += 1
    toRemoveIndexList.sort(reverse = True)
    for number in toRemoveIndexList:
        hand.pop(number)
    return hand

def dealRest(deck, pHand, lHand, uHand, rHand, dList, d, bSuit):
    #This function deals the rest of the cards from the deck to the hands
    while True:
        if (dList[0] != d):
            notD = dList.pop(0)
            dList.append(notD)
        else:
            dList.pop(0)
            dList.append(d)
            break
    counter = 0
    for word in dList:
        counter += 1
        if (counter == 4):
            break
        elif (word == "left"):
            deck, lHand = fillTo6(deck, lHand)
        elif (word == "up"):
            deck, uHand = fillTo6(deck, uHand)
        elif (word == "right"):
            deck, rHand = fillTo6(deck, rHand)
        elif (word == "player"):
            deck, pHand = fillTo6(deck, pHand)
        else:
            print("SOMETHING WENT WRONG IN dealRest() PART 1")
    if (dList[3] == "left"):
        lHand = fillRest(deck, lHand)
        lHand = removeExtra(lHand, bSuit)
    elif (dList[3] == "up"):
        uHand = fillRest(deck, uHand)
        uHand = removeExtra(uHand, bSuit)
    elif (dList[3] == "right"):
        rHand = fillRest(deck, rHand)
        rHand = removeExtra(rHand, bSuit)
    elif (dList[3] == "player"):
        pHand = fillRest(deck, pHand)
        pHand = removeExtra(pHand, bSuit)
    else:
        print("SOMETHING WENT WRONG IN dealRest() PART 2")

def fillTo6(deck, hand):
    #This function fills a hand to 6 cards with cards from a deck
    while (len(hand) < 6):
        hand.append(deck[len(deck)-1])
        deck.pop(len(deck)-1)
    return deck, hand

def fillRest(deck, hand):
    #This function fills a hand with all the cards left in a deck
    for card in deck:
        hand.append(card)
    return hand

def removeExtra(hand, bidSuit):
    #This function removes cards from a hand until the hand has 6 cards
    #This function does not remove the sent suit or 5s of the opposite suit
    if (bidSuit == "Hearts"):
        offSuit = "Diamonds"
    elif (bidSuit == "Diamonds"):
        offSuit = "Hearts"
    elif (bidSuit == "Spades"):
        offSuit = "Clubs"
    elif (bidSuit == "Clubs"):
        offSuit = "Spades"
    counter = 1
    while (len(hand) > 6):
        if (hand[len(hand)-counter].suit != bidSuit):
            if (hand[len(hand)-counter].suit != offSuit):
                hand.pop(len(hand)-counter)
            elif (hand[len(hand)-counter].value != "5"):
                hand.pop(len(hand)-counter)
            else:
                counter += 1
        elif (counter > 6):
            hand.pop(len(hand-1))
        else:
            counter += 1
    return hand

def playCards(pHand, lHand, uHand, rHand, lList, bidSuit):
    #This functions gets the card every player will play and prints to the screen
    pCardPlayed = None
    lCardPlayed = None
    uCardPlayed = None
    rCardPlayed = None

    printScreen(pHand, lHand, uHand, rHand, pCardPlayed, lCardPlayed, uCardPlayed, rCardPlayed)
    time.sleep(1)
    
    for word in lList:
        if (lList[0] == "player"):
            firstCardPlayed = pCardPlayed
        elif (lList[0] == "left"):
            firstCardPlayed = lCardPlayed
        elif (lList[0] == "up"):
            firstCardPlayed = uCardPlayed
        elif (lList[0] == "right"):
            firstCardPlayed = rCardPlayed
        
        if (word == "player"):
            pHand, pCardPlayed = getPlayerPlay(pHand, firstCardPlayed, bidSuit)
        elif (word == "left"):
            lHand, lCardPlayed = getPlay(lHand, firstCardPlayed, bidSuit)
        elif (word == "up"):
            uHand, uCardPlayed = getPlay(uHand, firstCardPlayed, bidSuit)
        elif (word == "right"):
            rHand, rCardPlayed = getPlay(rHand, firstCardPlayed, bidSuit)

        printScreen(pHand, lHand, uHand, rHand, pCardPlayed, lCardPlayed, uCardPlayed, rCardPlayed)
        time.sleep(1)

    return pHand, lHand, uHand, rHand, pCardPlayed, lCardPlayed, uCardPlayed, rCardPlayed

def getPlayerPlay(hand, fCardPlayed, bidSuit):
    #This function asks the player what card they want to play and validates if they can play it
    if (bidSuit == "Hearts"):
        offSuit = "Diamonds"
    elif (bidSuit == "Diamonds"):
        offSuit = "Hearts"
    elif (bidSuit == "Spades"):
        offSuit = "Clubs"
    elif (bidSuit == "Clubs"):
        offSuit = "Spades"

    if (fCardPlayed == None):
        test = False
    elif (fCardPlayed.suit == bidSuit):
        test = True
    elif (fCardPlayed.suit == offSuit and fCardPlayed.value == "5"):
        test = True
    else:
        test = False

    hasValid = False
    for card in hand:
        if (card.suit == bidSuit or (card.suit == offSuit and card.value == "5")):
            hasValid = True
    
    while (True):
        try:
            cardString = str(input("What card would you like to play? (Format input like 'K of Spades'): ")).upper()
            cardStringList = cardString.split(" ")
            if (cardStringList[2][0].lower() == "h"):
                tempSuit = "Hearts"
            elif (cardStringList[2][0].lower() == "c"):
                tempSuit = "Clubs"
            elif (cardStringList[2][0].lower() == "d"):
                tempSuit = "Diamonds"
            elif (cardStringList[2][0].lower() == "s"):
                tempSuit = "Spades"
            else:
                print("That isn't a valid suit.")
                continue
            hit = False
            for card in hand:
                if (cardStringList[0][0] == card.value or cardStringList[0] == card.value):
                    hit = True
                    if (tempSuit == card.suit):
                        if (test and card.suit == bidSuit):
                            hand.remove(card)
                            return hand, card
                        elif (test and card.suit == offSuit and card.value == "5"):
                            hand.remove(card)
                            return hand, card
                        elif (not test):
                            hand.remove(card)
                            return hand, card
                        elif (not hasValid):
                            hand.remove(card)
                            return hand, card
            if (not hit):
                print("You don't have that card.")
            else:
                print("You can't play that card.")
            continue
        except:
            print("Please format input properly")

def getPlay(hand, fCardPlayed, bidSuit):
    #This function calculates what card to play from a hand
    #It is used to get cards from the computer contolled players
    if (bidSuit == "Hearts"):
        offSuit = "Diamonds"
    elif (bidSuit == "Diamonds"):
        offSuit = "Hearts"
    elif (bidSuit == "Spades"):
        offSuit = "Clubs"
    elif (bidSuit == "Clubs"):
        offSuit = "Spades"

    if (fCardPlayed == None):
        test = True
    elif (fCardPlayed.suit == bidSuit):
        test = True
    elif (fCardPlayed.suit == offSuit and fCardPlayed.value == "5"):
        test = True
    else:
        test = False

    hasValid = False
    for card in hand:
        if (card.suit == bidSuit or (card.suit == offSuit and card.value == "5")):
            hasValid = True

    for card in hand:
        if (test and hasValid):
            if (card.suit == bidSuit or (card.suit == offSuit and card.value == "5")):
                hand.remove(card)
                return hand, card
        else:
            hand.remove(card)
            return hand, card

def getTrickWinner(wCard1, tCard1, wCard2, tCard2, bidSuit, lastWinner):
    #This funcrion calculates which team took the trick
    #And calculates how many points each team took
    wasTwo = False
    points = 0
    wePoints = 0
    theyPoints = 0
    
    if (bidSuit == "Hearts"):
        offSuit = "Diamonds"
    elif (bidSuit == "Diamonds"):
        offSuit = "Hearts"
    elif (bidSuit == "Spades"):
        offSuit = "Clubs"
    elif (bidSuit == "Clubs"):
        offSuit = "Spades"

    cards = [wCard1, tCard1, wCard2, tCard2]
    tempCards = [wCard1, tCard1, wCard2, tCard2]

    toRemove = []
    counter = 0
    for card in tempCards:
        if (card.suit == bidSuit):
            pass
        elif (card.suit == offSuit and card.value == "5"):
            pass
        else:
            toRemove.append(counter)
        counter += 1

    toRemove.sort(reverse = True)

    for number in toRemove:
        tempCards.pop(number)

    if (tempCards == []):
        return 0, 0, lastWinner

    orderList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    indexList = []

    for card in tempCards:
        indexList.append(orderList.index(card.value))

    for index in indexList:
        if (index == 0):
            wasTwo = True
            points += 1
        elif (index == 3):
            points += 5
        elif (index == 8):
            points += 1
        elif (index == 9):
            points += 1
        elif (index == 12):
            points += 1

    highIndex = 0
    for index in indexList:
        if (index > highIndex):
            highIndex = index

    winningCard = tempCards[indexList.index(highIndex)]
    winningCardIndex = cards.index(winningCard)

    if (winningCardIndex == 0):
        wePoints = points
        winner = "player"
    elif (winningCardIndex == 1):
        theyPoints = points
        winner = "left"
    elif (winningCardIndex == 2):
        wePoints = points
        winner = "up"
    elif (winningCardIndex == 3):
        theyPoints = points
        winner = "right"

    try:
        if (wasTwo):
            if (cards[0].value == "2" and cards[0].suit == bidSuit and wePoints == 0):
                wePoints += 1
                theyPoints -= 1
            elif (cards[2].value == "2" and cards[2].suit == bidSuit and wePoints == 0):
                wePoints += 1
                theyPoints -= 1
            elif (cards[1].value == "2" and cards[1].suit == bidSuit and theyPoints == 0):
                wePoints -= 1
                theyPoints += 1
            elif (cards[3].value == "2" and cards[3].suit == bidSuit and theyPoints == 0):
                wePoints -= 1
                theyPoints += 1
    except:
        pass

    return wePoints, theyPoints, winner

    
def main():
    #The main function that controls the operation of functions

    #pdb.set_trace()

    giveInstructions()

    gameOver = False
    handsPlayed = 0
    weScore = 0
    theyScore = 0
    
    #While game not over
    while (not gameOver):

        playerHand, leftHand, upHand, rightHand, deck = reset()

        playerHand = sortCards(playerHand)
        leftHand = sortCards(leftHand)
        upHand = sortCards(upHand)
        rightHand = sortCards(rightHand)
        
        printScreen(playerHand, leftHand, upHand, rightHand, None, None, None, None)

        #For testing purposes
##        printCards(leftHand)
##        printCards(upHand)
##        printCards(rightHand)
##        print()

        dealer, dealerList, handsPlayed = getDealer(handsPlayed)
        
        bid, bidSuit, bidder = getBids(dealer, dealerList, playerHand, leftHand, upHand, rightHand)
        if (bidSuit == None):
            bidSuit = getPlayerBidSuit()

        print(bidder + " got the bid for " + str(bid) + " in " + bidSuit)

        time.sleep(2)

        playerHand, leftHand, upHand, rightHand = discardExtraCards(playerHand, leftHand, upHand, rightHand, bidSuit)
        
        #For testing purposes
##        printScreen(playerHand, leftHand, upHand, rightHand, None, None, None, None)
##        printCards(leftHand)
##        printCards(upHand)
##        printCards(rightHand)
##        print()


        dealRest(deck, playerHand, leftHand, upHand, rightHand, dealerList, dealer, bidSuit)

        #For testing purposes
##        printScreen(playerHand, leftHand, upHand, rightHand, None, None, None, None)
##        printCards(leftHand)
##        printCards(upHand)
##        printCards(rightHand)
##        print()

        #Sorts the dealerList with the bidder first
        while True:
            if (dealerList[0] != bidder):
                notB = dealerList.pop(0)
                dealerList.append(notB)
            else:
                break

        leadList = dealerList
        wePointsTotal = 0
        theyPointsTotal = 0
        
        #while cards in hands
        while (len(playerHand) > 0 and (len(leftHand) > 0 or len(upHand) > 0 or len(rightHand) > 0)):
            
            playerHand, leftHand, upHand, rightHand, playerCardPlayed, leftCardPlayed, upCardPlayed, rightCardPlayed = playCards(playerHand, leftHand, upHand, rightHand, leadList, bidSuit)

            wePoints, theyPoints, winner = getTrickWinner(playerCardPlayed, leftCardPlayed, upCardPlayed, rightCardPlayed, bidSuit, leadList[0])
            print(winner + " won the hand.")
            wePointsTotal += wePoints
            theyPointsTotal += theyPoints

            while True:
                if (leadList[0] != winner):
                    notB = leadList.pop(0)
                    leadList.append(notB)
                else:
                    break

        handsPlayed += 1

        if (bidder == "player" or bidder == "up"):
            if (wePointsTotal >= bid):
                weScore += wePointsTotal
                theyScore += theyPointsTotal
            else:
                weScore -= bid
                theyScore += theyPointsTotal
        elif (bidder == "left" or bidder == "right"):
            if (theyPointsTotal >= bid):
                theyScore += theyPointsTotal
                weScore += wePointsTotal
            else:
                theyScore -= bid
                weScore += wePointsTotal

        print("We: " + str(weScore))
        print("They: " + str(theyScore))

        if ((weScore > theyScore) and (weScore >= 52)):
            print("You won! Congratulations!")
            gameOver = True
        elif ((theyScore > weScore) and (theyScore >= 52)):
            print("You lost! How sad :(")
            gameOver = True

main()
input()
