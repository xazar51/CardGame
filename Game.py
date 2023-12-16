from Card import Card, PlayingCard


class Game:
    def __init__(self):
        self._cards: list[Card] = []
        pass

    def add_card(self, suit: str, value: str) -> None:
        self._cards.append(PlayingCard(suit, value))
        pass

    def card_string(self, card: int) -> str:
        return self._cards[card].__str__()

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self._cards[card_a] > self._cards[card_b]
