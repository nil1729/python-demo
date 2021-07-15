from game_objects import Deck
from game_methods import setup_players, choose_chips, take_bet, hit, hit_or_stand, show_some, show_all, player_busts, player_wins, dealer_busts, dealer_wins, push


def start_game():
    """
    Main Game Logic and playing the game
    """
    # Print an opening statement
    print(f"\n {'*'*10} Welcome to BLACK JACK! {'*'*10}\n")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle_cards()

    # Set up the Players
    player_hand, dealer_hand = setup_players(deck)

    # Set up the Player's chips
    player_chips = choose_chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    playing_status = True

    while playing_status:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        playing_status = hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
    
        # Show all cards
        show_all(player_hand, dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"\nPlayer: {player_hand.name}'s winnings stand at {player_chips.total}")
    
    # Ask to play again
    new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        start_game()
    else:
        print(f"\n{'*'*10} Thanks for Playing! {'*'*10}\n")