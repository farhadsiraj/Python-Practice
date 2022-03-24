import random
from collections import deque


suits = (
    "Clubs",
    "Diamonds",
    "Hearts",
    "Spades",
)
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Deck_Stack:
    def __init__(self):
        self.all_cards = deque([])

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} card(s)."

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # Adding a list of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # Adding a single card
            self.all_cards.append(new_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)


class Player_Stack:
    def __init__(self, name):
        self.name = name
        self.all_cards = deque([])

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} card(s)."

    def remove_card(self):
        return self.all_cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # Adding a list of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # Adding a single card
            self.all_cards.append(new_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)


def print_deck(deck):
    for card_object in deck:
        print(card_object)


# Game Setup
while True:
    game_type = input("Select the game speed. Enter 'f' for Fast or 's' for Slow\n")

    if game_type[0].lower() in ["f", "s"]:
        break
    else:
        print("Sorry, please try again.")
        continue


# Feature Flag Toggle
fast = False
if game_type[0].lower() == "f":
    fast = True


def set_speed():
    global player_one, player_two, new_deck, num_cards

    if fast == True:
        player_one = Player_Stack("One")
        player_two = Player_Stack("Two")
        new_deck = Deck_Stack()
        num_cards = 10

        return player_one, player_two, new_deck, num_cards
    else:
        player_one = Player("One")
        player_two = Player("Two")
        new_deck = Deck()
        num_cards = 5

        return player_one, player_two, new_deck, num_cards


set_speed()

new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0


# End of game logic
while game_on:
    round_num += 1
    print(f"Round {round_num}")
    print("Player 1", len(player_one.all_cards))
    print("Player 2", len(player_two.all_cards))

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One wins!")
        game_on = False
        break

    # Start a new Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    # While at war
    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            player_one.shuffle()

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            player_two.shuffle()
            at_war = False

        else:
            print("WAR!")

            if len(player_one.all_cards) < num_cards:
                print("Player One unable to wage war")
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < num_cards:
                print("Player Two unable to wage war")
                print("Player One Wins!")
                game_on = False
                break

            else:
                for num in range(num_cards):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
