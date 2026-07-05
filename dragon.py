from boss import Boss
from items import Item

class Dragon(Boss):
    def __init__(self):

        super().__init__(
            name="Ancient Dragon",
            health=300,
            attack=40,
            defense=25,
            level=5,
            gold_drop=300,
            exp_drop=500,
            vitality=122,
            speed=40
        )

    def special_attack(self):
        print(f"{self.name} uses Fire Breath!")
        return self.attack * (2.5 + self.level * 0.35)

  
    def basic_attack(self):
       
       print(f"{self.name} bites the player!")
       return self.attack * (1 + self.level * 0.2)


    def drop_loot(self):

      loot = []

      loot.append(Item(
        name="Dragon Scale Armor",
        description="Armor made from dragon scales",
        defense_bonus=25,
        price=0,
        required_level=10
    ))

      loot.append(Item(
        name="Dragon Sword",
        description="Weapon forged from dragon fire",
        price=0,
        required_level=10,
        attack_bonus=30
    ))

      return loot   
    
    
    def defend(self):
        print(f"{self.name} raises its scales and reduces incoming damage!")
        return self.defense * (1 + self.level * 0.25)
        

    def check_phase(self):

        if (
            not self.phase_two
            and self.health <= self.max_health * 0.5
        ):

            self.phase_two = True

            self.attack = int(self.attack * 1.25)
            self.defense = int(self.defense * 1.15)

            print("\n🔥 The Dragon becomes enraged! 🔥")
            print("Attack and Defense increased!")       