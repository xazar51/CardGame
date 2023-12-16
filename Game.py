from typing import List

from Card import Card, PlayingCard, Joker, Hand


class Game:
    def __init__(self):
        self._cards: list[Card] = []
        self._hands: list[Hand] = []

    def add_card(self, suit: str, value: str) -> None:
        self._cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        return self._cards[card].__str__()

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self._cards[card_a] > self._cards[card_b]

    def add_joker(self, color: str) -> None:
        self._cards.append(Joker(color))

    def add_hand(self, card_indices: List[int]) -> None:
        self._hands.append(Hand([self._cards[i] for i in card_indices]))

    def hand_string(self, hand: int) -> str:
        return str(self._hands[hand])

    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        return self._hands[hand_a] > self._hands[hand_b]