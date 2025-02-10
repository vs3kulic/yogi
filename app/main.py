from app.game import Game

def main():
    game = Game()
    player = game.select_character(1)
    opponent = game.select_opponent()
    scores = game.run_round(player, opponent)
    result = game.declare_winner(scores)
    print(result)

if __name__ == "__main__":
    main()