from enemy import Enemy

class Skeleton(Enemy):
    def __init__(self, name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed):
        super().__init__(name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed)

    def basic_attack(self):
        if self.level <= 5:
            return self.attack * 1.3
        
        elif self.level <= 10:
            return self.attack * 1.8
        
        elif self.level > 10:
            return self.attack * 3
        
        return self.attack
    
    def special_attack(self):
        if self.level <= 5:
            return int(self.attack * 1.6)
        
        elif self.level <= 10:
            return self.attack * 2.5
        
        elif self.level > 10:
            return self.attack * 4.5
        
        return self.attack
           
    def defend(self):
        if self.level <= 5:
            return self.defense * 1.2
        
        elif self.level <= 10:
            return self.defense * 1.8
        
        elif self.level > 10:
            return self.defense * 3
        
        return self.defense
    
  

