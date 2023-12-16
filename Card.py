from enum import Enum, auto


class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        self.card_value < other.card_value


class Suit(Enum):
    # Automatically assign values to suits
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class PlayingCard(Card):
    SUITS = {
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES
    }

    SUIT_NAMES = {key: value for value, key in SUITS.items()}

    VALUES = {
        "A": "1",
        **{str(i): i for i in range(2, 11)},
        "J": "11",
        "Q": "12",
        "K": "13"
    }

    VALUE_NAMES = {key: value for value, key in VALUES.items()}

    def __init__(self, suit: str, value: str):
        super.__init__()
        self._suit = self.SUITS[suit]
        self._value = self.VALUES[value]

    @property
    def card_value(self) -> int:
        return self._value

    def __str__(self):
        suit = self.SUIT_NAMES[self._suit]
        value = self.VALUE_NAMES[self._value]
        return f"{value} of {suit}"
class Color(Enum):
    RED = auto()
    BLACK = auto()

class JokerCard(Card):
    COLORS = {"Red" : Color.RED,
              "Black" : Color.BLACK}

    COLOR_NAMES = {key:value for value,key in COLORS.items()}

    def __init__(self, color):
        super.__init__()
        self._color = self.COLORS[color]

    @property
    def card_value(self) -> int:
        return 14

    def __str__(self):
        color = self.COLOR_NAMES[self._color]
        return f"{color} Joker"
