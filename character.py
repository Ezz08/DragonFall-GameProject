from abc import ABC, abstractmethod
class Character(ABC):
    CountCharacters = 0
    def __init__(self, name, health, attack, defense, vitality):
        self.name = name
        self.health = health 
        self.attack = attack
        self.defense = defense
        self.vitality = vitality
        Character.CountCharacters += 1

    @abstractmethod
    def basic_attack(self):
        pass    

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def special_attack(self):
        pass

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0 

    def heal(self):
        self.health += self.vitality
        return self.health        

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"
    
