from boss import Boss
from items import Item

class Dragon(Boss):
    def __init__(self):

        super().__init__(
            name="Ancient Dragon",
            health=100,
            attack=65,
            defense=40,
            level=5,
            gold_drop=500,
            exp_drop=1000,
            vitality=122,
            speed=40
        )

    def special_attack(self, player):
        print(f"{self.name} uses Fire Breath!")
        return self.attack * 2

  
    def basic_attack(self, player):

       print(f"{self.name} bites the player!")
       return self.attack


    def drop_loot(self):

      loot = []

      loot.append(Item(
        name="Dragon Scale Armor",
        description="Armor made from dragon scales",
        defense_bonus=60,
        price=0,
        required_level=10
    ))

      loot.append(Item(
        name="Dragon Sword",
        description="Weapon forged from dragon fire",
        price=0,
        required_level=10,
        attack_bonus=70
    ))

      return loot   
    
    
    def defend(self):
        print(f"{self.name} raises its scales and reduces incoming damage!")
        return self.defense * 2
        

    def check_phase(self):

        if (
            not self.phase_two
            and self.health <= self.max_health * 0.5
        ):

            self.phase_two = True

            self.attack += 20
            self.defense += 10

            print("\n🔥 The Dragon becomes enraged! 🔥")
            print("Attack and Defense increased!")       
