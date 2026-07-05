from character import Character
from inventory import Inventory

class Player(Character):
    CountPlayers = 0
    def __init__(self, name, health, attack, defense, level, vitality, speed, exp):
        super().__init__(name, health, attack, defense, vitality)
        self.level = level
        self.exp = exp
        self.vitality = vitality
        self.speed = speed
        self.gold = 0
        self.equipped_weapon = None
        self.equipped_armor = None
        self.speed_potion_active = False
        self.inventory = Inventory()
        Player.CountPlayers += 1
  
    def basic_attack(self):
      attack = self.attack

      weapon = self.equipped_weapon
      if weapon:
        attack += weapon.attack_bonus

      level_multiplier = 1 + (self.level * 0.15)
      attack *= level_multiplier

      return attack
                      
    
    @property
    def defend(self):
     defense = self.defense

     armor = self.equipped_armor
     if armor:
        defense += armor.defense_bonus

     level_multiplier = 1 + (self.level * 0.12)
     defense *= level_multiplier

     return defense
    
    def use_health_potion(self):

      potion = self.inventory.search_item("Health Potion")


      if not potion:
          print("No Health Potion available!")
          return


      if self.health >= 100:
          print("HP is already full!")
          return

      self.health = min(self.health + potion.vitality_bonus, 100)


      self.inventory.remove_item(potion)

      print(f"Used Health Potion! HP is now {self.health}")

        
    def use_speed_potion(self):

      potion = self.inventory.search_item("Speed Potion")

      if not potion:
        print("No Speed Potion available!")
        return

      if self.speed_potion_active:
        print("Speed already active!")
        return

      self.speed_potion_active = True

      self.inventory.remove_item(potion)

      print("⚡ Speed Potion activated!")   
 
    def special_attack(self):
      attack = self.attack

      level_multiplier = 1 + (self.level * 0.25)
      attack *= level_multiplier

      return attack      
  
    def earn_gold(self, amount):
        self.gold += amount
        return self.gold
    
    def spend_gold(self,amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def basic_attack_target(self,enemy):
        damage = self.basic_attack()

        enemy.take_damage(damage)

        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def special_attack_target(self,enemy):
        damage = self.special_attack()

        enemy.take_damage(damage)

        print(f"{self.name} attacks {enemy.name} for {damage} damage!")  

    def gain_exp(self, amount):
      self.exp += amount

      xp_needed = 100 * (1.5 ** (self.level - 1))

      while self.exp >= xp_needed:
        self.exp -= xp_needed
        self.level += 1

        print(f"LEVEL UP! Now level {self.level}")

      xp_needed = 100 * (1.5 ** (self.level - 1))


    def get_display_stats(self):
      return {
        "attack": self.basic_attack(),
        "defense": self.defend,
        "health": self.health,
        "level": self.level,
        "exp": self.exp
      }
    
    def __str__(self):
      stats = self.get_display_stats()

      return (
        f"Name: {self.name}\n"
        f"Health: {stats['health']}\n"
        f"Attack: {stats['attack']}\n"
        f"Defense: {stats['defense']}\n"
        f"Level: {stats['level']}\n"
        f"Vitality: {self.vitality}\n"
        f"Speed: {self.speed}\n"
        f"EXP: {stats['exp']}"
      )