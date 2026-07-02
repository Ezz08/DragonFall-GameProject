from enemy import Enemy

class DarkMage(Enemy):
    def __init__(self, name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed):
        super().__init__(name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed)

    def basic_attack(self):
        if self.level <= 5:
            return self.attack * 1
        
        elif self.level <= 10:
            return self.attack * 3
        
        elif self.level > 10:
            return self.attack * 6
        
        return self.attack
    
    def special_attack(self):
        if self.level <= 5:
            return self.attack * 2
        
        elif self.level <= 10:
            return self.attack * 4
        
        elif self.level > 10:
            return self.attack * 8
        
        return self.attack
           
    
    def defend(self):
        if self.level <= 5:
            return self.defense * 1
        
        elif self.level <= 10:
            return self.defense * 3
        
        elif self.level > 10:
            return self.defense * 6
        
        return self.defense
    
  

