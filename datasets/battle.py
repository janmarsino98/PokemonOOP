class Battle:
    def __init__(self, trainer1, trainer2):
        self.turn = 0
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        
    def start_turn(self):
        self.turn += 1
        print(f"Starting turn {self.turn}")
        print(f"**************************")
        
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
                chosen_movenent = self.trainer1.select_movement()
                if chosen_movenent.target == "own":
                    chosen_movenent.target = self.trainer1.inbattlefieldpokemon
                elif chosen_movenent.target == "enemy":
                    chosen_movenent.target = self.trainer2.inbattlefieldpokemon
                else:
                    chosen_target_number = None
                    while chosen_target_number not in ["1", "2"]:
                        print(f"Who do you want to use {chosen_movenent.name} on?")
                        print(f"1. Your {self.trainer1.inbattlefieldpokemon.name}")
                        print(f"2. Enemy's {self.trainer2.inbattlefieldpokemon.name}")
                        chosen_target_number = input("Your choice: ")
                        if chosen_target_number == "1":
                            chosen_movenent.target = self.trainer1.inbattlefieldpokemon
                        elif chosen_target_number == "2":
                            chosen_movenent.target = self.trainer2.inbattlefieldpokemon
                        
                print(f"{self.trainer1.name}'s {self.trainer1.inbattlefieldpokemon.name} used {chosen_movenent.name}")
                self.trainer1.inbattlefieldpokemon.attack_enemy(chosen_movenent, chosen_movenent.target)
            
            else:
                print(self.determine_winner())
                
            self.end_turn()