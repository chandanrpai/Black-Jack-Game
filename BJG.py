#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print(' ')

## The possible card values range from 1 to 10 and, unlike a real deck, the probability of drawing a card is equal.
## The game begins by dealing two visible cards to the player (face up), and two cards to the dealer.
## However, in the case of the dealer, one card is visible to other players while the other is hidden.
## The player decides whether to "hit" (draw another card), or "stand" which ends their turn.
## The player may hit any number of times. 
## Should the total of the cards exceed 21, the player "busts" and loses the game to the dealer.
## If the player reaches 21, the player stands.
## The dealer's turn begins by revealing the hidden card
## The dealer must hit if the total is 16 or less, and must stand if the value is 17 or more
## The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)
## The program indicates who the winner is and asks to play again
## Note the game includes face card and ACE will be designated a value of 11

class Card(object):
    card_values = {'Ace': 11,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

def cv(x):
    card_values = {'Ace': 11,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}
    pts = card_values[x]
    return pts
        
def ascii_version_of_card(*cards, return_string=True):
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]
    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank[0]  # 'King' changes to 'K' ("King" doesn't fit)
            space = ' '  
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string

    lines = [
    ['┌─────────┐'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['└─────────┘']
            ]
    # store the non-flipped over card after the one that is flipped over
    cards_except_first = ascii_version_of_card(*cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)
        
        


print('Welcome to Blackjack.')
print('---------------------------------------------------------------------------------')

while True:
    print(' ')
    print('---------------------------------------------------------------------------------')
    print(' ')
    deck = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suts = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    
    print('Do you wish to start a new game? (y/n):')
    NG = input()
    if (NG == "y" or NG == "Y"):
        #print('Note: Ace will have a value of 11 in this game')
        import subprocess as sp
        sp.call('cls',shell=True)
        import random
        PC1 = random.choice(deck)
        PC1V= cv(PC1)
        PC1ST = random.choice(suts)
        PC2 = random.choice(deck)
        PC2V = cv(PC2)
        PC2ST = random.choice(suts)
        PCT=[0 for i in range(10)]
        i=0
        PCT[i] = PC1V+PC2V
        print(f'You draw a {PC1ST} {PC1} and a {PC2ST} {PC2}. Your total is {PCT[i]}.')
        print(ascii_version_of_card(Card(PC1ST, PC1), Card(PC2ST, PC2)))
        DC1 = random.choice(deck)
        DC1V = cv(DC1)
        DC1ST = random.choice(suts)
        DC2 = random.choice(deck)
        DC2V = cv(DC2)
        DC2ST = random.choice(suts)
        DCT = DC1V + DC2V
        print(f'The dealer draws a {DC1ST} {DC1} and a hidden card.')
        print(ascii_version_of_hidden_card(Card(DC2ST, DC2), Card(DC1ST, DC1)))
        if (PCT[i]==21):
            print(f'You stand with a perfect total of {PCT[i]}.')
            PA1 = "s" 
        else:
            print('Hit or stand? (h/s):')
            PA1 = input()
        while True:         
            if (PA1 == "h" or PA1 == "H"):
                CNX = random.choice(deck)
                CNXV = cv(CNX)
                CNXST = random.choice(suts)
                i+=1
                PCT[i]=PCT[i-1]+CNXV
                if (PCT[i]>21):
                    print(f'Game Over. You drew {CNXST} {CNX}. Your total is {PCT[i]}, which is over 21.')
                    print(ascii_version_of_card(Card(CNXST, CNX)))
                    break      
                if (PCT[i]==21):
                    print(f'You drew {CNXST} {CNX}.You stand with a perfect total of {PCT[i]}. ')
                    print(ascii_version_of_card(Card(CNXST, CNX)))
                    PA1 = "s"  
                    #HERE
                else:
                    print(f'Hit! You draw a {CNXST} {CNX}. Your total is {PCT[i]}.')
                    print(ascii_version_of_card(Card(CNXST, CNX)))
                    print(f' Hit or stand? (h/s):')
                    #HERE
                    PA1 = input()
            elif (PA1 == "s" or PA1 == "S"):
                print(f'Dealers hidden card is {DC2ST} {DC2}. Dealer total is {DCT}')
                print(ascii_version_of_card(Card(DC2ST, DC2), Card(DC1ST, DC1)))
                if(DCT>16):               
                        if (PCT[i]>DCT):
                            print(f'You Win!')
                        elif (PCT[i]==DCT):
                            print(f'Dealer wins all ties. Play agin.')
                        else:
                            print(f'You lost. Good luck next time')
                        break
                        
                while(DCT<=16):
                    print(f'Dealer draws a card agian')
                    DC3 = random.choice(deck)
                    DC3V = cv(DC3)
                    DC3ST = random.choice(suts)
                    DCT += DC3V
                    if(DCT>21):
                        print(f'You Win! Dealer busted on drawing {DC3ST} {DC3}. Dealer total is {DCT}')
                        print(ascii_version_of_card(Card(DC3ST, DC3)))
                        break
                    elif(DCT>16):
                        print(f'Dealer Draws {DC3ST} {DC3}. Dealer total is {DCT}. Dealer Stands.')
                        print(ascii_version_of_card(Card(DC3ST, DC3)))
                        if (PCT[i]>DCT):
                            print(f'You Win!')
                        elif (PCT[i]==DCT):
                            print(f'Dealer wins all ties. Play agin.')
                        else:
                            print(f'You lost. Good luck next time')
                        break
                    else:
                        print(f'Dealer draws {DC3ST} {DC3}. Dealer total is {DCT}')
                        print(ascii_version_of_card(Card(DC3ST, DC3)))
                break
            else:
                print('Only H/S values are allowed, please enter your choice again:')
                PA1 = input()
    elif (NG == "n" or NG == "N"):
        print('Thank you! Hope to see you again.')
        break
    else:
        print('Only Y/N values are allowed, please enter your choice again:')

