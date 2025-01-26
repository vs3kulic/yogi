import random
from game_data import main_characters, antagonists

class Game: 
    def __init__(self):
        self.main_characters = main_characters 
        self.antagonists = antagonists

    def select_character(self):
        print("Select a main character:")
        for index, character in enumerate(self.main_characters):
            print(f"{index + 1}. {character.name} ({character.race})")
        
        choice = int(input("Enter the number of your choice: ")) -1 
        if 0 <= choice < len(self.main_characters):
            fighter = self.main_characters[choice]
            print(f"You picked {fighter.name} as your fighter!")
            return fighter
        else:
            print("Invalid choice. Please try again.")
            return self.select_character()
        
    def select_opponent(self):
        print("Your opponent will be chosen at random...") 
        opponent = random.choice(self.antagonists)
        print(f"Your opponent is {opponent.name}!")
        return opponent

    def coin_toss(self): 
        print("A coin will be tossed to determine who goes first...")
        pick = input("Heads or tails? ").lower()
        print(f"You picked {pick}!")
        print("The coin is in the air...")
        coin = random.choice(["heads", "tails"])
        print(f"The coin landed on {coin}!")
        if pick == coin:
            print("You won the toss and go first!")
            return True
        else:
            print("You lost the toss and go second!")
            return False 

    def run_round(self, player, opponent):
        player_turn = self.coin_toss()
        
        while player.life_points > 0 and opponent.life_points > 0: 
            if player_turn:
                damage = player.attack(opponent)
                print(f"{player.name} attacks {opponent.name} for {damage} damage!")
                print(f"{opponent.name} has {opponent.life_points} life points left.")
            else:
                damage = opponent.attack(player)
                print(f"{opponent.name} attacks {player.name} for {damage} damage!")
                print(f"{player.name} has {player.life_points} life points left.")
            player_turn = not player_turn
        
        if player.life_points > opponent.life_points:
            winner = player
            return winner
        else: 
            winner = opponent
            return winner

    def declare_winner(self, winner):
        print(f"{winner.name} wins the battle!")