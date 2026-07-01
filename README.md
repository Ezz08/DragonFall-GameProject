# ⚔️ Dragonfall: Ashen Curse

A terminal-based RPG game built with Python featuring turn-based combat, quests, inventory system, merchants, leveling, save/load system, and a final dragon boss fight.

# 🎮 About The Game
Dragonfall: Ashen Curse is a text-based RPG where the player fights enemies, completes quests, collects loot, upgrades stats, and faces a final boss dragon. The game is built using Python OOP principles and focuses on strategy, progression, and survival.

# 📖 Story

In the land of **Eldoria**, peace was shattered when an ancient beast known as the **Ancient Dragon** awakened. It was not just a monster, but the origin of a dark curse that spread across the world.

From the dragon’s corrupted energy, the **Dark Mage** was born, mastering forbidden dark magic. He raised an army of the undead—**Skeletons**—to protect his secrets and spread chaos across the land.

Meanwhile, in the ruined forests, **Goblins** emerged, taking advantage of the chaos to become thieves and mercenaries, serving any power that guarantees their survival.

You are the last hope of this world…

Your mission is to stop the chain of destruction:

🧙 Dark Mage → ☠ Skeleton Army → 👾 Goblins → 🔥 Ancient Dragon

And bring peace back to Eldoria once again.

# 🧠 Features
⚔️ Turn-based combat system with basic & special attacks, dodge and defense mechanics.  
👾 Multiple enemies including Goblin, Skeleton, Dark Mage, and Ancient Dragon boss.  
🧾 Quest system with kill-based objectives and reward system.  
🛒 Merchant system for buying weapons, potions, and upgrades.  
🎒 Inventory system with item usage and management.  
📊 Leveling system with EXP and scaling difficulty.  
💾 Save and Load system for full game progress persistence.

# 🧱 Project Structure
GameProject/
├── main.py
├── Game.py
├── player.py
├── enemy.py
├── Quest.py
├── inventory.py
├── seller.py
├── items.py
├── goblin.py
├── skeleton.py
├── DarkMage.py
├── dragon.py
├── ui.py
└── save.json

# ▶️ How to Run
Install Python, pyfiglet library, rich library, open terminal in project folder, then run:
python main.py

# 🎮 Controls
1 → Basic Attack  
2 → Special Attack  
3 → Use Health Potion  
4 → Use Speed Potion  

Enemy Turn:  
1 → Defend  
2 → Dribble / Dodge  

# 💾 Save System
The game saves:
Player stats, inventory, quests progress, gold, EXP, and level scaling. You can load full progress anytime from the main menu.

# 🔥 Future Improvements
Add animations in terminal, better UI design, sound effects, more enemies, skill trees, and improved AI behavior.

# 👨‍💻 Developer Notes
Built using Python OOP concepts: classes, inheritance, polymorphism, composition, game loops, and state management.

# ⚔️ Enjoy The Game
Fight, survive, and defeat the Ancient Dragon!
