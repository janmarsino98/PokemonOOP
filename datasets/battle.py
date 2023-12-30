class Battle:
    def __init__(self, trainer1, trainer2):
        self.turn = 0
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        
    def start_turn(self):
        self.turn += 1
        print(f"Starting turn {self.turn}")
        
    def end_turn(self):
        print(f"The turn {self.turn} ended.")
        
            
    def determine_winner(self):
        
        if not self.trainer1.has_active_pokemon() and not self.trainer2.has_active_pokemon():
            print(f"The battle ended in a draw since none of the player have a pokemon alive.")
            winner = "Ninguno"
            
        elif not self.trainer1.has_active_pokemon():
            print(f"The winner is {self.trainer2.name}.")
            winner = self.trainer2.name
            
        elif not self.trainer2.has_active_pokemon():
            print(f"The winner is {self.trainer1.name}.")
            winner = self.trainer1.name
            
        else:
            print("There is no winner yet.")
            winner = None
            
        return winner
            
        
    def battle_loop(self):           
        while self.trainer1.has_active_pokemon() and self.trainer2.has_active_pokemon():
            self.start_turn()
            
            if self.turn == 1:
                self.trainer1.set_battlefield_pokemon(self.trainer1.pokemons[0])
                self.trainer2.set_battlefield_pokemon(self.trainer2.pokemons[0])
                
            if self.determine_winner() == None:
                print(f"{self.trainer1.name} needs to select which movement is {self.trainer1.inbattlefieldpokemon.name} going to use")
                chosen_movenent = self.trainer1.inbattlefieldpokemon.select_movement()
                self.trainer1.inbattlefieldpokemon.attack_enemy(chosen_movenent, self.trainer2.inbattlefieldpokemon)
            
            
            self.end_turn()
            exit()