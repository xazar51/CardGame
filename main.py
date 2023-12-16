from Game import Game

if __name__ == '__main__':
    game = Game()
    hand_a_list = []
    n_1 = int(input())
    for i in range(n_1):
      suit, value = input().split()
      game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
      hand_a_list.append(i)
    game.add_hand(hand_a_list)
    print("\n")
    print(game.hand_string(0))
    hand_b_list = []
    n_2 = int(input())
    for i in range(n_1, n_1 + n_2):
      suit, value = input().split()
      game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
      hand_b_list.append(i)
    game.add_hand(hand_b_list)
    print(game.hand_string(1))
    print("true" if game.hand_beats(0, 1) else "false")