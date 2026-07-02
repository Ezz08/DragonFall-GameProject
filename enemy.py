from character import Character
from abc import ABC, abstractmethod

class Enemy(Character, ABC):
    enemy_count = 0
    def __init__(self, name, health, attack, defense, level, gold_drop, exp_drop , vitality, speed):
        super().__init__(name, health, attack, defense, vitality)
        self.level = level
        self.vitality = vitality
        self.speed = speed
        self.gold_drop = gold_drop
        self.exp_drop = exp_drop
        Enemy.enemy_count += 1

    def give_reward(self, player):
        if self.health <= 0:
            player.earn_gold(self.gold_drop)
            return self.gold_drop  
    
    @abstractmethod
    def basic_attack(self):
        pass

    @abstractmethod
    def special_attack(self):
        pass


    def basic_attack_target(self, player):
        damage = self.basic_attack()

        player.take_damage(damage)

        print(f"{self.name} attacks {player.name} for {damage} damage!")     

    def special_attack_target(self, player):
        damage = self.special_attack()

        player.take_damage(damage)

        print(f"{self.name} attacks {player.name} for {damage} damage!")

    def __str__(self):
        return f"{super().__str__()}, Level: {self.level}, Gold Drop: {self.gold_drop}, EXP Drop: {self.exp_drop}, Vitality: {self.vitality}, Speed: {self.speed}"     