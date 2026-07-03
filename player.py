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
        self.speed_potion_active = False
        self.inventory = Inventory()
        Player.CountPlayers += 1
  
    def basic_attack(self):
      attack = self.attack

      sword = self.inventory.search_item("Iron Sword")
      arrow = self.inventory.search_item("Arrow")
      potion = self.inventory.search_item("Attack Potion")
      dragon_sword = self.inventory.search_item("Dragon Sword")

      if self.level <= 3:
        attack *= 1.2

      elif 4 <= self.level <= 5:
        attack *= 1.8

      elif 6 <= self.level <= 10:
        attack *= 2.6

      else:
        attack *= 3.5

      if sword:
        attack += sword.attack_bonus

      if arrow:
        attack += arrow.attack_bonus

      if potion:
        attack += potion.attack_bonus

      if dragon_sword:
        attack += dragon_sword.attack_bonus

      return attack
                      
    
    @property
    def defend(self):
     defense = self.defense

     iron_shield = self.inventory.search_item("Iron Shield")
     leather_shield = self.inventory.search_item("Leather Shield")
     dragon_armor = self.inventory.search_item("Dragon Scale Armor")

    
     if self.level <= 3:
        defense *= 1.2

     elif 4 <= self.level <= 5:
        defense *= 1.6

     elif 6 <= self.level <= 10:
        defense *= 2.2

     else:
        defense *= 3   

     if iron_shield:
        defense += iron_shield.defense_bonus

     if leather_shield:
        defense += leather_shield.defense_bonus

     if dragon_armor:
        defense += dragon_armor.defense_bonus         

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

      if self.level <= 3:
        attack *= 2

      elif 4 <= self.level <= 5:
        attack *= 2.5

      elif 6 <= self.level <= 10:
        attack *= 3.2

      else:
        attack *= 4.5

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

        while self.exp > self.level * 100:
            self.exp -= self.level * 100
            self.level += 1

            print(f"{self.name} leveled up!")


    def __str__(self):
        return f"{super().__str__()}, Level: {self.level}, Vitality: {self.vitality}, speed: {self.speed}, exp: {self.exp}"