"""
Black Jack Game Methods
    take_bet => Player bets
"""
from game_objects import Chips, Hand

def setup_players(deck):
    """
    Create a list of players and their names
    """
    while True:
        try: 
            name = input("Enter the name of the player: ")

        except ValueError: 
            print("Sorry, a player must be a string. Please try again: ")
            continue

        else:
            player = Hand(name)
            dealer = Hand("Computer")

            for x in range(2):
                player.add_card(deck.deal())
                dealer.add_card(deck.deal())
            break

    return player, dealer

def choose_chips():
    """
    Method: choose_chips()
    Description: Asks the player how many chips they want to play with.
    Input: None
    Output: The number of chips the player wants to play with.
    """
    while True:
        try:
            chips = Chips()
            chips.total = int(input("Enter the number of chips you would like to play with: "))
        
        except ValueError:
            print("Sorry, a chip must be an integer! Please try again: ")
            continue       
        
        else:
            if chips.total < 1:
                print("Sorry, a chip must be greater than 0. Please try again: ")
                continue       
            else:
                break       
    return chips

def take_bet(chips):
    """
    Ask the player how many chips they want to bet
    """
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))

        except ValueError:
            print('Sorry, a bet must be an integer! which don\'t exceeds your current total chips')
            continue

        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed your chips total ", chips.total)
            else:
                break

def hit(deck, hand):
    """
    Draw a card from the deck and add it to the player's or Dealer's hand
    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    """
    Prompt player to Hit or Stand
    """
    while True:
        choose_option = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")
        
        if choose_option[0].lower() == 'h':
            hit(deck, hand)
            return True

        elif choose_option[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            return False

        else:
            print("Sorry, please try again. Enter 'h' or 's' only: ")
            continue

def show_some(player, dealer):
    """
    Show the player's and dealer's cards
    """
    print("\nDealer's Hand:")
    print("First Card Hidden")
    print(dealer.cards[1])

    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print(f"Value of Player's Hand: {player.value}")


def show_all(player, dealer):
    """
    Show the player's and dealer's cards
    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print(f"Value of Dealer's Hand: {dealer.value}")

    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print(f"Value of Player's Hand: {player.value}")


def player_busts(player, dealer, chips):
    """
    Player busts
    """
    print(f"Player {player.name} Busts! Dealer {dealer.name} Wins!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    """
    Player wins
    """
    print(f"Player {player.name} Wins! Dealer {dealer.name} Lost the game!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    """
    Dealer busts
    """
    print(f"Dealer {dealer.name} Busts! Player {player.name} Wins!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    """
    Player looses
    """
    print(f"Dealer {dealer.name} Wins! Player {player.name} Lost the game!")
    chips.lose_bet()

def push(player, dealer):
    """
    Push
    """
    print(f"Dealer {dealer.name} and Player {player.name} tie! It's a push.")
