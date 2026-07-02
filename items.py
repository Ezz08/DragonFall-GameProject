class Item:
    def __init__(self, name, description, price, required_level, attack_bonus=0, defense_bonus=0, vitality_bonus=0, speed_bonus=0):
        self.name = name
        self.description = description
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.vitality_bonus = vitality_bonus
        self.speed_bonus = speed_bonus
        self.required_level = required_level
        self.price = price
    
    