from player import Player
from enemy import Enemy
from seller import Seller
from goblin import Goblin
from skeleton import Skeleton
from DarkMage import DarkMage
from dragon import Dragon
from items import Item
from Quest import Quest
import random
from inventory import Inventory
import json
from ui import game_title, main_menu_panel, character_menu_panel, inventory_menu_panel, battle_menu_panel, quest_menu_panel, shop_menu_panel
from ui import game_title

class Game:
    def __init__(self):
        self.player = Player(
            name = "Leo",
            health = 100,
            attack = 20,
            defense = 10,
            level = 1,
            vitality = 5,
            speed = 10,
            exp=0
        )

        self.seller = Seller([
            Item(
                 name="Health Potion",
                 description="Restores health",
                 price=15,
                 required_level=1,
                 vitality_bonus=30
            ),

            Item(
                name="Arrow",
                description="increases attack",
                price=10,
                required_level=7,
                attack_bonus=5      
            ),

            Item(
                name="Speed Potion",
                description="increases speed",
                price=20,
                required_level=2,
                speed_bonus= 10     
            ),

            Item(
                name="Leather Shield",
                description="Basic Shield",
                price=30,
                required_level=4,
                defense_bonus=8      
            ),

            Item(
                name="Attack Potion",
                description="Boosts attack",
                price=40,
                required_level=5,
                attack_bonus=6      
            ),

            Item(
                name="Iron Sword",
                description="Strong sword",
                price=120,
                required_level=10,
                attack_bonus=15      
            ),

            Item(
                name="Iron Shield",
                description="Heavy Shield",
                price=90,
                required_level=8,
                defense_bonus=18     
            ),        
        ])

        self.boss = []
        self.boss.append(Dragon())


        self.quests = [
         self.create_quest("goblin"),
         self.create_quest("skeleton"),
         self.create_quest("darkmage"),
         self.create_quest("dragon")
         ]   


    def create_quest(self, quest_type):

         if quest_type == "goblin":
           
            quest = Quest(
               title="Goblin Hunter",
               target_enemy="Goblin",
               required_kills=3,
               reward_gold=60,
               repeatable=True
            )

            return quest


         elif quest_type == "skeleton":

              quest = Quest(
                title="Skeleton Slayer",
                target_enemy="Skeleton",
                required_kills=5,
                reward_gold=120,
                repeatable=True
              )

              return quest


         elif quest_type == "darkmage":

              quest = Quest(
                title="DarkMage Slayer",
                target_enemy="Darkmage",
                required_kills=7,
                reward_gold=250,
                repeatable=False
              )

              return quest


         elif quest_type == "dragon":

              quest = Quest(
                title="Dragon Slayer",
                target_enemy="Ancient Dragon",
                required_kills=1,
                reward_gold=800,
                repeatable=False
              )

         return quest
        

    def create_enemy(self, enemy_type):

       level = self.player.level

       if enemy_type == "goblin":

        return Goblin(
            name="Goblin",
            health=80,
            attack=10 + level * 2,
            defense=5 + level,
            level=level,
            gold_drop=10 + level * 3,
            exp_drop=15 + level * 5,
            vitality=5,
            speed=10
        )

       elif enemy_type == "skeleton":

        return Skeleton(
            name="Skeleton",
            health=120,
            attack=18 + level * 3,
            defense=10 + level * 2,
            level=level,
            gold_drop=25 + level * 5,
            exp_drop=30 + level * 8,
            vitality=15,
            speed=20
        )

       elif enemy_type == "darkmage":

        return DarkMage(
            name="DarkMage",
            health=150,
            attack=25 + level * 4,
            defense=15 + level * 3,
            level=level,
            gold_drop=50 + level * 8,
            exp_drop=60 + level * 12,
            vitality=32,
            speed=30
        )

       elif enemy_type == "dragon":

        return Dragon()
       

    def save_game(self):

     inventory_data = []

     for item in self.player.inventory.items:
        inventory_data.append(item.name)

     quests_data = []

     for quest in self.quests:
        quests_data.append({
            "title": quest.title,
            "current_kills": quest.current_kills,
            "completed": quest.completed,
            "reward_claimed": quest.reward_claimed,
            "repeatable": quest.repeatable
        })

     data = {
        "player": {
            "name": self.player.name,
            "health": self.player.health,
            "attack": self.player.attack,
            "defense": self.player.defense,
            "level": self.player.level,
            "gold": self.player.gold,
            "exp": self.player.exp,
            "vitality": self.player.vitality,
            "speed": self.player.speed
        },
        "inventory": inventory_data,
        "quests": quests_data
    }

     with open("save.json", "w") as file:
        json.dump(data, file, indent=4)

     print("Game Saved Successfully!")


    def load_game(self):

      with open("save.json", "r") as file:
        data = json.load(file)

      player = data["player"]

      self.player.name = player["name"]
      self.player.health = player["health"]
      self.player.attack = player["attack"]
      self.player.defense = player["defense"]
      self.player.level = player["level"]
      self.player.gold = player["gold"]
      self.player.exp = player["exp"]
      self.player.vitality = player["vitality"]
      self.player.speed = player["speed"]

    # Inventory
      self.player.inventory.items.clear()

      for item_name in data["inventory"]:

        item = self.seller.get_item(item_name)

        if item:
            self.player.inventory.add_item(item)

    # Quests
      for saved_quest in data["quests"]:

        for quest in self.quests:

            if quest.title == saved_quest["title"]:

                quest.current_kills = saved_quest["current_kills"]
                quest.completed = saved_quest["completed"]
                quest.reward_claimed = saved_quest["reward_claimed"]
                quest.repeatable = saved_quest["repeatable"]

      print("Game Loaded Successfully!")
       

    def equip_weapon(self):

      weapons = []

      for item in self.player.inventory.items:
        if item.attack_bonus > 0:
            weapons.append(item)

      if not weapons:
        print("You don't have any weapons!")
        return

      print("\n=== WEAPONS ===")

      for i, weapon in enumerate(weapons, start=1):
        print(f"{i}. {weapon.name} (+{weapon.attack_bonus} ATK)")

      choice = input("Choose weapon: ")

      if not choice.isdigit():
        return

      choice = int(choice)

      if 1 <= choice <= len(weapons):
        self.player.equipped_weapon = weapons[choice - 1]
        print(f"✅ Equipped {weapons[choice - 1].name}")

    def equip_armor(self):

      armors = []

      for item in self.player.inventory.items:
        if item.defense_bonus > 0:
            armors.append(item)

      if not armors:
        print("You don't have any armor!")
        return

      print("\n=== ARMORS ===")

      for i, armor in enumerate(armors, start=1):
        print(f"{i}. {armor.name} (+{armor.defense_bonus} DEF)")

      choice = input("Choose armor: ")

      if not choice.isdigit():
        return

      choice = int(choice)

      if 1 <= choice <= len(armors):
        self.player.equipped_armor = armors[choice - 1]
        print(f"✅ Equipped {armors[choice - 1].name}")

    def unequip_weapon(self):

     if self.player.equipped_weapon is None:
         print("No weapon equipped.")
         return

     print(f"Unequipped {self.player.equipped_weapon.name}")

     self.player.equipped_weapon = None

    def unequip_armor(self):

     if self.player.equipped_armor is None:
        print("No armor equipped.")
        return

     print(f"Unequipped {self.player.equipped_armor.name}")

     self.player.equipped_armor = None   
    
    
    def main_menu(self):

        while True:
            game_title()
            main_menu_panel()

            choice = input("Choose:")

            if choice == "1":
                self.character_menu()

            elif choice == "2":
                print(self.inventory_menu())

            elif choice == "3":
                self.battle_menu()

            elif choice == "4":
                self.quest_menu()

            elif choice == "5":
                self.shop_menu()

            elif choice == "6":
                self.save_game()

            elif choice == "7":
                self.load_game()

            elif choice == "8":
                break

    def character_menu(self):

        while True:
            game_title()
            character_menu_panel()

            choice = input("choose:") 

            if choice == "1":
                print(self.player.__str__())

            elif choice == "2":
                self.show_enemies()

            elif choice == "3":
                self.show_bosses()

            elif choice == "4":
                break 

    def show_enemies(self):

      print("\n=== ENEMIES ===")

      enemies = [
        self.create_enemy("goblin"),
        self.create_enemy("skeleton"),
        self.create_enemy("darkmage")
      ]

      for enemy in enemies:
         print(enemy)

    def show_bosses(self):

        print("\n=== BOSS ===")

        for boss in self.boss:
            print(boss)  


    def inventory_menu(self):

       while True:
          game_title()
          inventory_menu_panel()

          choice = input("Choose:") 

          if choice == "1":
             print(self.player.inventory.__str__())

          elif choice == "2":

             item_name = input("Enter Item Name:")

             item = self.player.inventory.search_item(item_name)

             if item:
                print(item.name)
             else:
                print("Item not Found")

          if choice == "3":
           self.equip_weapon()

          elif choice == "4":
           self.equip_armor()

          elif choice == "5":
           self.unequip_weapon()

          elif choice == "6":
           self.unequip_armor()

          elif choice == "7":
             item_name = input("Enter item name: ")

             item = self.player.inventory.search_item(item_name)      

             if item:

                self.player.inventory.remove_item(item)
             else:
              print(f"Item not found in inventory.")   
   

          elif choice == "8":
           return    

    def quest_menu(self):

       while True:
          game_title()
          quest_menu_panel()

          choice = input("choose:")

          if choice == "1":
             self.show_quests()

          elif choice == "2":
             self.claim_rewards()

          elif choice == "3":
             break

    def show_quests(self):
       
       print("\n=== QUESTS ===")

       for quest in self.quests:
          print(quest)  


    def claim_rewards(self):

     quest_name = input("Enter quest title: ")

     for quest in self.quests:

        if quest.title.lower() == quest_name.lower():

            quest.claim_reward(self.player)
            return

    def shop_menu(self):

     while True:

        print("\n=== MERCHANT ===")
        print(f"Player's Gold: {self.player.gold}")
        print(f"Player's level: {self.player.level}")

        self.seller.show_items(self.player)

        game_title()
        shop_menu_panel()

        choice = input("Choose: ")

        if choice == "1":
                        
            item_name = input("Enter item name: ")
            self.seller.buy_item(self.player, item_name)

        elif choice == "2":
            break         


    def battle_menu(self):

      while True:
        game_title()
        battle_menu_panel()

        choice = input("Choose: ")

        if choice == "1":
            result = self.battle(self.create_enemy("goblin"))

            if result == "main_menu":
                break

        elif choice == "2":
            result = self.battle(self.create_enemy("skeleton"))

            if result == "main_menu":
                break

        elif choice == "3":
            result = self.battle(self.create_enemy("darkmage"))

            if result == "main_menu":
                break

        elif choice == "4":
            dragon = self.create_enemy("dragon")
            result = self.battle_dragon(dragon)

            if result == "main_menu":
                break

        elif choice == "5":
            break

    def battle(self, enemy):
       
       print("Battle started")
       print("Player HP:", self.player.health)
       print("Enemy HP:", enemy.health)

       turn = "player"
       
       player_special_cooldown = 0

       print(f"A wild {enemy.name} appeared!")
                      
       while self.player.health > 0 and enemy.health > 0: 

          print("\n━━━━━━━━━━━━━━━━━━━━━━")
          print(f"{self.player.name}: {self.player.health}")
          print(f"{enemy.name}: {enemy.health}")
          print("━━━━━━━━━━━━━━━━━━━━━━\n")

          if turn == "player":

           print("\n=== YOUR TURN ===")
           print("1. Basic Attack")

           if player_special_cooldown == 0:
            print("2. Special Attack")

           if self.player.inventory.has_item("Health Potion"):
            print("3. Health Potion") 

           if self.player.inventory.has_item("Speed Potion"):
            print("4. Speed Potion")

           choice = input("Choose:") 

           if choice == "1":
             attack = self.player.basic_attack()
             defense = enemy.defend()

             damage = int(max(0, attack - defense))

             enemy.take_damage(damage)

             print(f"{self.player.name} attacks {enemy.name} for {damage} damage!")

             if enemy.health <= 0:
               return self.victory(enemy)      

           elif choice == "2":

             if player_special_cooldown == 0:

                attack = self.player.special_attack()
                defense = enemy.defend()

                damage = int(max(0, attack - defense))

                enemy.take_damage(damage)

                print(f"{self.player.name} attacks {enemy.name} for {damage} damage!")

                if enemy.health <= 0:
                  result = self.victory(enemy)
                  return result
                
                player_special_cooldown = 2

             else:

                print(
                    f"Special Attack available after "
                    f"{player_special_cooldown} rounds."
                )     

                continue

           elif choice == "3":
             self.player.use_health_potion()

             continue

           elif choice == "4":
             self.player.use_speed_potion()

             continue
           
           else:
             print("Invalid choice!")
             continue
          
             
           turn = "enemy"

          elif turn == "enemy":
                  
           print("\n=== ENEMY TURN ===")
           print("1. Defend")
           print("2. Dribble")    

           defend_choice = input("Choose: ")

           if defend_choice == "1":
             
             damage =  int(max(0, enemy.basic_attack() - self.player.defend))

             if damage < 0:
                damage = 0

             self.player.take_damage(damage)

             if self.player.health <= 0:
                  result = self.game_over(enemy)
                  return result

             print(f"You blocked part of the attack!")
             print(f"You received {damage} damage.")

           elif defend_choice == "2":

             if self.player.speed_potion_active:

                print("Perfect Dodge!")
                self.player.speed_potion_active = False   

             else:

                if random.randint(1,100) <= 50:
                     
                     print("You dodged successfully!")

               
                else:

                   damage = int(max(0, enemy.special_attack()))

                   self.player.take_damage(damage) 

                   if self.player.health <= 0:
                     result = self.game_over(enemy)
                     return result

                   print("Dodge Failed!")
                   print(f"You received {damage} damage.") 

             if player_special_cooldown > 0:
              player_special_cooldown -= 1 

           else:
             print("invalid choice!")
             continue 
          
           turn = "player"
           continue
                         

  
    def game_over(self, enemy):

       print("\n===== GAME OVER =====")
       print(f"You were defeated by {enemy.name}!")

       print(f"Level : {self.player.level}")
       print(f"Gold  : {self.player.gold}")
       print(f"EXP   : {self.player.exp}")

       print("\n1. Retry")
       print("2. Main Menu")
       print("3. Exit")

       choice = input("Choose: ")

       if choice == "1":
          
           self.player.health = 100
           if enemy.name == "Goblin":
             enemy = self.create_enemy("goblin")
           elif enemy.name == "Skeleton":
             enemy = self.create_enemy("skeleton")
           elif enemy.name == "DarkMage":
             enemy = self.create_enemy("darkmage")
           return self.battle(enemy)

       elif choice == "2":
          
          self.player.health = 100
          return "main_menu"
       
       else:
         
         exit()   


    def victory(self, enemy):

      print(f"\n===== VICTORY =====")
      print(f"You defeated {enemy.name}!")

      gold = enemy.gold_drop
      exp = enemy.exp_drop

      self.player.health = 100

      print(f"You earned {gold} Gold!")
      print(f"You earned {exp} EXP!")

      self.player.earn_gold(gold)
      self.player.gain_exp(exp)

      for quest in self.quests:
        quest.update_progress(enemy.name)

      print("\n1. Continue")
      print("2. Main Menu")

      choice = input("Choose: ")

      if choice == "1":
         return 
  
      if choice == "2":
         return "main_menu"            

                  
    def battle_dragon(self, dragon):
       
       print("Battle started")

       turn = "player"
       
       player_special_cooldown = 0

       print(f"\n🔥 FINAL BOSS: {dragon.name} appears!")

       while self.player.health > 0 and dragon.health > 0:
                   
          dragon.check_phase()

          print("\n==============================")
          print(f"Player: {self.player.health} HP")
          print(f"{dragon.name}: {dragon.health} HP")
          print("==============================")

          if turn == "player":

           print("\n=== YOUR TURN ===")
           print("1. Basic Attack")

           if player_special_cooldown == 0:
             print("2. Special Attack")

           if self.player.inventory.has_item("Health Potion"):
             print("3. Health Potion")

           if self.player.inventory.has_item("Speed Potion"):
             print("4. Speed Potion")

           choice = input("Choose: ")

           if choice == "1":
            self.player.basic_attack_target(dragon)
            if dragon.health <= 0:
                return self.dragon_victory_menu(dragon)

           elif choice == "2":
            self.player.special_attack_target(dragon)
            if dragon.health <= 0:
                return self.dragon_victory_menu(dragon)

           elif choice == "3":
            self.player.use_health_potion()
            continue

           elif choice == "4":
            self.player.use_speed_potion()
            continue
           
           elif choice == "":
            print("Please choose an action!")
            continue
           
           else:
             print("Invalid choice!")
             continue
           
           turn = "dragon"

          elif turn == "dragon": 

           print("\n=== DRAGON TURN ===")
           print("1. Defend")
           print("2. Dribble")

           defend_choice = input("Choose: ")

           if defend_choice == "1":
             
             damage = int(max(0, dragon.basic_attack() - self.player.defend))

             if damage < 0:
                damage = 0

             self.player.take_damage(damage)

             if self.player.health <= 0:
                 result = self.dragon_game_over()
                 return result

             print(f"You blocked part of the attack!")
             print(f"You received {damage} damage.")

           elif defend_choice == "2":

             if self.player.speed_potion_active:

                print("Perfect Dodge!")
                self.player.speed_potion_active = False   

             else:

                if random.randint(1,100) <= 50:
                     
                     print("You dodged successfully!")

               
                else:

                   damage = int(max(0, dragon.special_attack()))

                   self.player.take_damage(damage) 

                   if self.player.health <= 0:
                     result = self.dragon_game_over()
                     return result

                   print("Dodge Failed!")
                   print(f"You received {damage} damage.")       

           else:
            print("Invalid choice!")
            continue        

           turn = "player"
           continue

          if player_special_cooldown > 0:
            player_special_cooldown -= 1
          

          if dragon.health <= 0:
            result = self.dragon_victory_menu(dragon)
            return result

    def dragon_game_over(self):

      print("\n===== GAME OVER =====")
      print("You were defeated by the Ancient Dragon!")

      print(f"Level : {self.player.level}")
      print(f"Gold  : {self.player.gold}")
      print(f"EXP   : {self.player.exp}")

      print("\n1. Retry")
      print("2. Main Menu")
      print("3. Exit")

      choice = input("Choose: ")

      if choice == "1":

        self.player.health = 100

        dragon = Dragon()

        return self.battle_dragon(dragon)

      elif choice == "2":
        
        self.player.health = 100
        return "main_menu" 

      elif choice == "3":

        exit()   


    def dragon_victory_menu(self, dragon):

      print("\n🔥🔥 DRAGON DEFEATED! 🔥🔥")
      print("================================")
      print("1. Take Rewards")
      print("2. View Loot")
      print("3. Exit to Main Menu")
      print("================================")

      choice = input("Choose: ")

      gold = dragon.gold_drop
      exp = dragon.exp_drop

      if choice == "1":
         
         if dragon.reward_claimed:
          print("Already claimed!")
          return "main_menu"
         
         print(f"\n💰 You earned {gold} Gold!")
         print(f"⭐ You gained {exp} EXP!")

         self.player.earn_gold(gold)
         self.player.gain_exp(exp)

         dragon.reward_claimed = True

         for quest in self.quests:
            quest.update_progress(dragon.name)

         self.player.health = 100
         return "main_menu"  

      elif choice == "2":
        loot = dragon.drop_loot()

        print("\n🎁 Loot Dropped:")
        for item in loot:
            print(f"- {item.name}")
            self.player.inventory.add_item(item)
            print("ITEM ADDED:", item.name)
            print("CURRENT INVENTORY:", [i.name for i in self.player.inventory.items])

        return self.dragon_victory_menu(dragon)

      else:
        print("Returning to main menu...")
        self.player.health = 100
        return "main_menu"   
