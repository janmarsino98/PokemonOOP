class Pokemon:
    def __init__(self, name, level, health, attack, defense, speed, speattack, spedefense, typ, movements):
        self.name = name
        self.level = level
        self.health = health
        self.baseattack = attack
        self.basedefense = defense
        self.basespeed = speed
        self.basespeattack = speattack
        self.basespedefense = spedefense

        self.attackbuff = 0
        self.defensebuff = 0
        self.speedbuff = 0
        self.speattackbuff = 0
        self.spedefensebuff = 0
        
        self.attack = self.baseattack * (1 + self.attackbuff * 0.5)
        self.defense = self.basedefense * (1 + self.defensebuff * 0.5)
        self.speed = self.basespeed * (1 + self.speedbuff * 0.5)
        self.speattack = self.basespeattack * (1 + self.speattackbuff * 0.5)
        self.spedefense = self.basespedefense * (1 + self.spedefensebuff * 0.5)
    
        self.movements = movements
        
    def attack(self, enemy):
        selected_movement = int(input(f"Choose one of your movemnents:\n1.{self.movements[9]}\n2.´{self.movements[1]}\n3.{self.movements[2]}\n4.{self.movements[3]}"))
        print(selected_movement.name)
        