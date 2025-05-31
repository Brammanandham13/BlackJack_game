import random
from art import logo
print(logo)
"""Deal both user and computer a starting hand of 2 random card values."""

#step-1
def deal_card():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


 # if 11 in cards and 10 in cards and len(cards)==2: //checking dircet method
    #     return 0

#step-2
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    """Detect when computer or user has a blackjack. (Ace + 10 value card)"""
    """If computer gets blackjack, then the user loses (even if the user also has a blackjack). 
    If the user gets a blackjack, then they win (unless the computer also has a blackjack)."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    """If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead"""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
#step-7 compare
def compare_score(u_score,c_score):
    if u_score==c_score:
        return "DRWA"
    elif c_score==0:
        return "computer have blackjack user loose"
    elif u_score==0:
        return"win with the blackjack"
    elif u_score>21:
        return "u lose"
    elif c_score>21:
        return "computer wins user losse"
    elif u_score > c_score:
        return "user wins"
    else:
        return " u loose"



play=True
def play_game():
    #step-3 create an empty list and give random cards to user&computer
    user_card=[]
    computer_card=[]
    comp_sc=-1
    user_sc=-1
    """ not interfer the making decision for update the score """
    isgame=False

    """ only take two initial cards """
    for _ in range(2):
# step-4 add it in list
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not isgame:
        #step-5 call the function for  scores
        user_sc = calculate_score(user_card)
        comp_sc = calculate_score(computer_card)

        print(f"the user score is {user_card} and score is :----> {user_sc}")
        print(f"computer score :--->{comp_sc}")

        """Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack."""
        ## step-6 decide the game end point
        if user_sc==0 or comp_sc==0 or user_sc>21:
            isgame=True
        else:
            """Ask the user if they want to get another card."""
            user_should=input("want to drwa the card again type y or else type n\n")
            if user_should=="y":
                user_card.append(deal_card())
            else:
                isgame=True


    """Once the user is done and no longer wants to draw any more cards, let the computer play. 
    The computer should keep drawing cards unless their score goes over 16."""
    while comp_sc!=0 and comp_sc<17:
        """Compare user and computer scores and see if it's a win, loss, or draw."""
        computer_card.append(deal_card())
        comp_sc=calculate_score(computer_card)

    print(f"the user cards are {user_card} and the final score was {user_sc}")
    print(f"the user cards are {computer_card} and the final score was {comp_sc}")

    print(compare_score(user_sc,comp_sc))





while play:
    game=input("want u play ?type y or n\n")
    if game=="y":
        print("\n"*20)
        play_game()
    else:
        play=False
