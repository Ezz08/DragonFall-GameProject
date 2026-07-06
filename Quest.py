class Quest:
    def __init__(self, title, target_enemy, required_kills, reward_gold, repeatable):
        self.title = title
        self.target_enemy = target_enemy
        self.required_kills = required_kills
        self.current_kills = 0
        self.reward_gold = reward_gold
        self.completed = False
        self.reward_claimed = False
        self.repeatable = repeatable

    def update_progress(self, enemy_name):

      if enemy_name.lower().strip() != self.target_enemy.lower().strip():
        return

      self.current_kills += 1

      if self.current_kills >= self.required_kills:
        self.completed = True

    def claim_reward(self, player):

     if not self.completed:
        print("Quest is not completed yet!")
        return
     
     if self.reward_claimed:
        print("Reward already claimed!")
        return

     player.earn_gold(self.reward_gold)

     print(f"You claimed {self.reward_gold} Gold!")

     if self.repeatable:

        self.current_kills -= self.required_kills
        self.completed = self.current_kills >= self.required_kills

     else:
        
        self.reward_claimed = True 


    def __str__(self):

      status = "Completed" if self.completed else "In Progress"
      repeat = "Repeatable" if self.repeatable else "One-time"

      return (
        f"Quest: {self.title} | "
        f"Target: {self.target_enemy} | "
        f"Progress: {self.current_kills}/{self.required_kills} | "
        f"Reward: {self.reward_gold} Gold | "
        f"Status: {status} | "
        f"Type: {repeat}"
      ) 



    
                    