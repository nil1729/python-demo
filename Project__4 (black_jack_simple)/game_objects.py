"""
Black Jack Game Essential Objects
    Card
    Deck
    Hand
    Chips
"""

import random
from global_vars import suits, ranks, values

class Card:
    """
    Card Class

    Instance Variables(
        suit - Card suit,
        rank - Card rank,
    )

    __str__(self) = Prints rank and suit of Card, e.g. Ace of Diamonds
    __repr__(self) = Prints Card initialization e.g. Card('diamond', 'ace')
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'Card({self.suit}, {self.rank})'

class Deck:
    """
    Deck Class

    Instance Variables (
        deck - list of 52 cards
    )

    __str__() = Prints all cards in deck, e.g. Ace of Diamonds, ace of hearts, ace of spades ...

    methods
        shuffle_cards()
        deal()
    """
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def shuffle_cards(self):
        """
        this method shuffle the cards of the Deck (in-place shuffling)
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        this method take last card from the deck
        """
        return self.deck.pop()

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += f'\n{card}'
        return f'The Deck has: {deck_comp}'

class Hand():
    """
    Hand class (Representing a player's hand)

    Instance Variables (
        cards - list of cards currently on the player's hand,
        value - total value of the cards
        aces - number of aces in the hand
    )

    __str__(self) = Prints Player name, number of cards in hand with value and number of aces

    methods
        add_card(card)
        adjust_for_ace()
    """
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Add a card (Card Object) to the hand
        this card picked from the deck of 52 cards with the method of deck.deal()
        """
        self.cards.append(card)
        self.value += values[card.rank]

        # Track aces
        if card.rank == 'ace':
            self.aces += 1

    def adjust_for_ace(self):
        """
        If total value of hand is over 21 and I still have an ace, reduce my ace value by 10
        """
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        """
        String representation of player's hand
        """
        return f"""
            {self.name} has {len(self.cards)} Cards.
            Total value: {self.value}
            Total Aces: {self.aces}
            """

class Chips:
    """
    Chips class

    Instance Variables (
        total - player's total chips
        bet - player's current bet
    )

    methods
        win_bet()
        lose_bet()
    """
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        """
        if player won the bet, then add the bet to the total chips
        """
        self.total += self.bet

    def lose_bet(self):
        """
        if player lost the bet, then subtract the bet from the total chips
        """
        self.total -= self.bet
