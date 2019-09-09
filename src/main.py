from agents.randomagent import RandomAgent
from manager import GameManager

if __name__ == '__main__':
    game_manager = GameManager()
    player1 = RandomAgent()
    player2 = RandomAgent()
    for i in range(1000):
        if i % 2 == 0:
            game_manager.set_players(player1, player2)
        else:
            game_manager.set_players(player2, player1)

        game_manager.play()
        if i % 100 == 0:
            print(i)
    print("P1 win %: " + str(player1.get_wins() / (player1.get_wins() + player2.get_wins())))