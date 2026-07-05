from enemy import Enemy

class DarkMage(Enemy):
    def __init__(self, name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed):
        super().__init__(name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed)

    def basic_attack(self):
        return self.attack * (1 + self.level * 0.18)
    
    def special_attack(self):
        return self.attack * (2 + self.level * 0.3)
           
    
    def defend(self):
        return self.defense * (1 + self.level * 0.08)
    
  

