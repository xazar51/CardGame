from enum import Enum, auto


class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.card_value < other.card_value


class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class PlayingCard(Card):
    SUITS = {
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
    }
    SUIT_NAMES = {e: n for n, e in SUITS.items()}
    VALUES = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    VALUE_NAMES = {e: n for n, e in VALUES.items()}

    def __init__(self, suit: str, value: str):
        super().__init__()
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    @property
    def card_value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        value = self.VALUE_NAMES[self.__value]
        suit = self.SUIT_NAMES[self.__suit]
        return f'{value} of {suit}'


class JokerColor(Enum):
    RED = auto()
    BLACK = auto()


class Joker(Card):
    COLORS = {
        "Red": JokerColor.RED,
        "Black": JokerColor.BLACK,
    }

    COLOR_NAMES = {e: n for n, e in COLORS.items()}

    def __init__(self, color: str):
        super().__init__()
        self.__color = self.COLORS[color]

    @property
    def card_value(self):
        return 14

    def __str__(self) -> str:
        return f"{self.COLOR_NAMES[self.__color]} Joker"


class Hand:
    def __init__(self, cards):
        super().__init__()
        self.cards = [*cards]

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)

    def __lt__(self, other):
        for card_a, card_b in zip(reversed(sorted(self.cards)), reversed(sorted(other.cards))):
            if card_a < card_b:
                return True
            elif card_b < card_a:
                return False
        return False
