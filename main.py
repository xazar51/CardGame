import Game

if __name__ == '__main__':
    game = Game()
    suit, value = input().split()
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = input().split()
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
