import random

#Setting overall game conditions on startup below: game_over Boolean condition set to False, and a global
#chips_balance variable that begins at 0 everytime one plays
#it does not reset every deal just every actual game it will reset at 0.

game_over = False
dealer = print('Welcome to Blackjack! I will be your dealer today.')
chips_balance = 0 # default chip balance to begin the game

# Creating the standard deck of cards as dictionary in which I call the values in order to determine the value of the cards
# Later in I will multiply this by 4 in order to obtain a standard card deck of 52 cards.

Cards = ('A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
Values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

#Here I create classes to structure my game by way of Card, Hand, Deck and Player. This gave me a stable foundation of methods/attributes to call
# if needed for the game.
class Card(object):

    #This allows the program to understand that I want to use the integer value of my cards oppose to the key
    #for example this allows 'K' to be interpreted as a value of 10 while the game is being played.

    def __init__(self, value):
        if(value in Values):
            self.value = Values[value]
        else:
            self.value = None
            print('Invalid Card')

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)

    #The Hand class allows the program to interpret a hand as a [list] of values according to the card the user obtains

class Hand(object):
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    #the blackjack and bust methods were created just for easy access to obtain print statements for either wins or losses
    # ** Never call the h.blackjack() in the game because I preferred differing custom statements for blackjack wins
    def blackjack(self):
        print('Congratulations, player! You just got blackjack and walking out a winner! Collect 50 chips')

    def bust(self):
        print('Sorry! You have busted. Loser. Lose 20 chips.')

class Deck(object):
    #Here I establish the Deck class, I begin by multiplying my dictionary values by 4 in order to incorporate 52
    #cards (values) in to the deck
    def __init__(self):
        self.deck = []
        for i in range(4):
            for value in Values:
                self.deck.append(str(Card(value)))
    #The deal card method uses the efficiency of .pop() in order to draw the first card from a deck either unshuffled
    #or shuffled
    def deal_card(self):
        return self.deck.pop()
    # This is one of the first methods I call in the start of the game in order to shuffle the 52 values in my deck
    def shuffle(self):
        random.shuffle(self.deck)

    # here I create the method of dealing the first two cards of the deck to the player and return them as strings.
    def deal_hand(self):
        return str(self.deal_card()), str(self.deal_card())
# Here is the player class, I have set the name of the player to Player 1
# and give made the class to return the same string at the start of every round.
class Player(object):
    def __init__(self, name= 'Player 1', chips= chips_balance):
        self.name = name
        self.bet = 1
        self.chips = chips

    def place_bet(self):
        return 'Let me see the cards I have left. I will place an intellectual bet for you!' + ' ' + 'Bet one chip!' + ' ' + 'Your current chip balance is' + ' ' + str(self.chips)

    def __str__(self):
        return 'Welcome Player 1! Please note if dealer wins you will lose 10 chips, if dealer gets BLACKJACK you will lose 25 chips. If you bust you will lose 20 chips. You will gain 10 chips for every card other than a 10 added to your hand. You will gain 1 chip for every 10 added to your hand. Finally, you will be awarded 50 chips for a Blackjack. Enjoy! Here is your first hand!'


#Sets a loop around the boolean function created earlier
while game_over == False:
    #The hand_total is a very important value in my game, I set it equal to 0 here so every game will begin with the
    # player hand value to be 0.
    hand_total = 0
    # Here I initiate the general game with calling in to play some classes and methods from above:
    # For example, the d.shuffle() function allows the deck to be shuffled before the start of every round. To ensure
    # randomness of card values every game.
    h = Hand()
    d = Deck()
    d.shuffle()

    # Now that I have ensured my deck is shuffled I start the game by calling the Player class which will show the __str__
   # method I created under the Player class
    play = Player()
    print (play)
    # This deals the player (Player 1) their first hand and shows it to them. Make players deem 'ACES' in first hands as ones by my choice
    # most of time it is used as a 1 early on anyway.
    p = d.deal_hand()
    print (p)
    # Here I deal the dealer a hand to oppose the player's
    q = d.deal_hand()

 # Below: I use ensure the program calculates the hand_total value correctly by adding up both cards dealt to both
    # the player and the dealer as integers to obtain a total value of the two cards.
    hand_total = (int(p[0]) + int(p[1]))
    dealer_total = (int(q[0]) + int(q[1]))
    # The first game winning command and call h.blackjack() method from the Hand class above if your first two cards add up to 21 then you are a winner
    # Also tells the program to add 50 chips to the players balance for achieving a blackjack
    ## I purposely do not give chips to player until they elect to 'hit' therefore is possible to end rounds even or with 0 chips

    if hand_total == 21:
        chips_balance = chips_balance + 50
        print('Winner bud. Congrats. Grab yourself 50 chips.')

    # main functionality loop of the blackjack game, while the user's hand_total value is less than 21 this tells the program to prompt them with the
    # the question of whether to add more card(s) to their hand or stay with current value

    while hand_total < 21: #no win or loss yet
            print("Would you like to hit or stay? h/s ")
            answer = str(input('Type h for hit or s for stay: '))
            if answer == 'h':
                #card creation, and value added to total. Also tells program whether to give use 1 or 10 chips based on the value of card added to their hand
                p2 = int(d.deal_card())
                if p2 == 10:
                    chips_balance = chips_balance + 1
                elif p2 == 1: # another user choice prompt, whether to count their Ace as a 1 or a eleven
                    print('You have been awarded an ACE. Would you like to count your Ace as a 1 or a 11?')
                    count = str(input('Type ele to count as a eleven. If you would like to count as a one type otherwise.'))
                    if count == 'ele':
                        p2 = 11
                        chips_balance = chips_balance + 1
                    else:
                        p2 = 1
                        chips_balance = chips_balance + 10
                else:
                    chips_balance = chips_balance + 10
                #Below by presenting += int(p2) this creates a running sum of 'hits' the user makes to their hand total. Needed so program does not reset hand_total to original hand after each hit.
                hand_total += int(p2)
                print('Current hand value after card addition: ' + str(hand_total) + ". You currently have " + str(chips_balance) + " chips.")

                if hand_total > 21: #lose condition by BUSTING
                    chips_balance = chips_balance - 20
                    print(h.bust())
                    print("Would you like to continue? EXIT to leave.")
                    y = str(input('Type y to play again! We would love to have you stay for another round!'))
                    if y == 'y':
                        break
                elif hand_total == 21: #winning condition
                    chips_balance = chips_balance + 50
                    print("BLACKJACK BLACKJACK BLACKJACK, congrats! You have been awarded 50 chips.")
                    print("Would you like to continue? EXIT to leave.")
                    y = str(input('Type y to play again! We would love to have you stay for another round!'))
                    if y == 'y':
                        break
                else:
                    continue
            elif answer == 's': # Eventually user must stay, therefore once 's' is pressed presents the user with the dealer's cards and based on below inequality and and statements determine whether user or dealer wins!
                print("The dealer nods and reveals his first card to be a " + str(int(q[0])) + ". Next card is ")
                print("a " + str(int(q[1])) + " for a total of " + str(dealer_total))
                if dealer_total >= 17 and dealer_total > hand_total:
                    print('Dealer has a hand total of ' + str(dealer_total) + '. You lose!')
                    chips_balance = chips_balance - 10
                elif dealer_total >= 17 and dealer_total < hand_total:
                    print('Dealer has a hand total of ' + str(dealer_total) + '. You win! Congrats')
                elif dealer_total == hand_total:
                    print('Wow, dealer has a score of ' + str(dealer_total) + '. Equal deals, No winner!')
                elif dealer_total < 17:
                    print("The Dealer hits again.")
                    d2 = d.deal_card()
                    # Again makes dealer's deck a running sum so they could hit multiple times if given abnormally low first hand.
                    dealer_total += int(d2)
                    if dealer_total == 21:
                        print('Wow dealer obtained a ' + str(int(d2)) + '. Dealer blackjack. You Lose')
                        chips_balance = chips_balance - 25
                    elif dealer_total < 21 and dealer_total < hand_total:
                        print('Dealer has a hand total of ' + str(dealer_total) + '. You win!')
                    elif dealer_total > 21 and hand_total <= 21:
                        print('Dealer has a hand total of ' + str(dealer_total) + '. Dealer busts, you won')
                    elif dealer_total < 21 and dealer_total > hand_total:
                        print("Dealer has a total of " + str(dealer_total) + ". You lose!")
                        chips_balance = chips_balance - 10
                    elif dealer_total == hand_total:
                        print('Wow, the dealer has a score of ' + str(dealer_total) + '. That means equal deals, no winner this round!')
                    elif dealer_total < hand_value1 or dealer_total < hand_total:
                        print("Dealer has a hand total of " + str(dealer_total) + ". You win!")
                elif dealer_total >= 17 and dealer_total > hand_total:
                    print("Dealer has a score of " + str(dealer_total) + ". You Lose!")
                    chips_balance = chips_balance - 10
                print("Would you like to continue? EXIT to leave.")
                y = str(input('Type y to play again! We would love to have you stay for another round!'))
                if y == 'y': # multiple statements like this included to ensure the program asks the user if they want to keep playing after each and every outcome!
                    break
            else:
                continue
    print("Thank you for Playing. Current Chip Balance: " + str(chips_balance))
    # Wanted to create an endgame print statement that let the user know how many chips they have. May make them keep playing :D.
