"""
    Simple Card War game using Python OOPs Concept

    suits - Tuple of suits,
    ranks - Tuple of ranks,
    values - Dictionary of rank, value pairs
"""
import random
suits = ('hearts', 'spades', 'diamonds', 'Clubs')
ranks = (
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'jack',
    'queen',
    'king',
    'ace'
)
values = {
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 11,
    'queen': 12,
    'king': 13,
    'ace': 14,
}

class Card:
    """
    Card Class

    Instance Variables(
        suit - Card suit,
        rank - Card rank,
        value - Card value for Comparison
    )
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'Card({self.suit}, {self.rank})'

    def __len__(self):
        return self.value

class Deck:
    """
    Deck Class

    Instance Variables (
        all_cards - list of 52 cards
    )

    methods
        shuffle_cards()
        deal_one_card()
    """
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle_cards(self):
        """
        this method shuffle the cards of the Deck (in-place shuffling)
        """
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        """
        this method take last card from the deck
        """
        return self.all_cards.pop()

class Player():
    """
    Player Class

    Instance Variables (
        all_cards - list of cards player have in their hands
        name - Player name
    )

    methods
        add_cards(new_cards)
        pick_card()
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        """
        this method add single and multiple cards to player card list
        """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def pick_card(self):
        """
        pick one card from top of the player card deck
        """
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} Cards in hand'

def check_winner(p_1, p_2, max_card=0):
    """
    Check which player is wins the game after each round
    """
    if len(p_1.all_cards) <= max_card:
        print(
            f"""
            Player One: {p_1.name}, out of cards.
            Player Two: {p_2.name} Wins this match
            """
        )
        return True

    if len(p_2.all_cards) <= max_card:
        print(
            f"""
            Player Two: {p_2.name}, out of cards.
            Player One: {p_1.name} Wins this match
            """
        )
        return True

    return False

def distribute_cards(deck, p_1, p_2):
    """
    Distribute the newly created deck cards to players
    """
    deck.shuffle_cards()
    total_cards = len(deck.all_cards)

    while total_cards > 0:
        p_1.add_cards(deck.deal_one_card())
        p_2.add_cards(deck.deal_one_card())
        total_cards -= 2

def war_winner(p_1, p_2, lpc_1, lpc_2, game_cards):
    """
    Check who wins the current war and make necessary adjustments.
    """
    if lpc_1.value > lpc_2.value:
        p_1.add_cards(game_cards)
        return True

    if lpc_1.value < lpc_2.value:
        p_2.add_cards(game_cards)
        return True

    return False


def play_game():
    """
    Start the game
    """
    game_on = True
    round_num = 0

    player_1 = Player(input('Enter Player One Name: '))
    player_2 = Player(input('Enter Player Two Name: '))
    new_deck = Deck()

    distribute_cards(new_deck, player_1, player_2)

    while game_on:
        round_num += 1
        print(f'Current Round: {round_num}')

        if check_winner(player_1, player_2):
            game_on = False
            break

        player_1_cards = []
        player_2_cards = []

        player_1_cards.append(player_1.pick_card())
        player_2_cards.append(player_2.pick_card())

        is_war = True
        while is_war:
            last_player_1_card = player_1_cards[-1]
            last_player_2_card = player_2_cards[-1]
            total_cards_on_war = player_1_cards + player_2_cards

            if war_winner(
                p_1=player_1,
                lpc_1=last_player_1_card,
                p_2=player_2,
                lpc_2=last_player_2_card,
                game_cards=total_cards_on_war
            ):
                is_war = False

            else:
                print('In war')

                if check_winner(player_1, player_2, max_card=5):
                    is_war = False
                    game_on = False

                else:
                    required_cards = 5
                    while required_cards > 0:
                        player_1_cards.append(player_1.pick_card())
                        player_2_cards.append(player_2.pick_card())
                        required_cards -= 1

play_game()
