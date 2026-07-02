from enemy import Enemy

class Boss(Enemy):
    def __init__(self, name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed):
        super().__init__(name, health, attack, defense, level, gold_drop, exp_drop, vitality, speed)

        self.max_health = health
        self.phase_two = False

    def special_attack(self,player):
        pass


    def check_phase(self):
            pass
    
    def drop_loot(self):
        pass