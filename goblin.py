from enemy import Enemy

class Goblin(Enemy):
    def __init__(self, name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed):
        super().__init__(name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed)

    def basic_attack(self):
        return self.attack * (1 + self.level * 0.1)
    
    def special_attack(self):
        return self.attack * (1.5 + self.level * 0.15)
           
    def defend(self):
        return self.defense * (1 + self.level * 0.08)
    
  

