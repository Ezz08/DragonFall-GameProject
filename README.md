# Dragonfall: Ashen Curse

A terminal-based RPG game built with Python featuring turn-based combat, quests, inventory management, merchants, leveling, save/load functionality, and a final boss battle.

# About the Game

Dragonfall: Ashen Curse is a text-based RPG built using Python and Object-Oriented Programming principles. The player fights enemies, completes quests, earns gold and experience, purchases equipment, manages an inventory, and prepares to defeat the Ancient Dragon.

The project was created to practice OOP concepts while building a complete RPG game from scratch.

# Story

In the land of **Eldoria**, peace was shattered when the **Ancient Dragon** awakened. Its dark curse spread across the kingdom, giving birth to the **Dark Mage**, who mastered forbidden magic and raised an army of **Skeletons**.

Meanwhile, **Goblins** emerged from the ruined forests, serving anyone powerful enough to ensure their survival.

As the last remaining hero, your mission is to defeat every threat standing between you and the Ancient Dragon to restore peace to Eldoria.

# Features

* Turn-based combat system
* Basic and Special Attacks
* Defense and Dodge mechanics
* Multiple enemy types
* Quest system
* Merchant system
* Inventory management
* Weapons and Armor equipment
* Health and Speed potions
* Leveling and EXP progression
* Save and Load system
* Final Ancient Dragon boss battle

# Project Structure

```text
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
├── save.json
└── requirements.txt
```

# Getting Started

## Dependencies

* Python 3.10+
* rich
* pyfiglet

## Installation

Clone the repository:

```bash
git clone https://github.com/Ezz08/DragonFall-GameProject.git
```

Move into the project folder:

```bash
cd GameProject
```

Install the required packages:

```bash
pip install -r requirements.txt
```

# Running the Game

```bash
python main.py
```

# Controls

Player Turn

* 1 → Basic Attack
* 2 → Special Attack
* 3 → Health Potion
* 4 → Speed Potion

Enemy Turn

* 1 → Defend
* 2 → Dodge

# Input Rules

* Enter menu options using numbers only.
* Do not type extra spaces.
* Item names must match the correct spelling.
* Capitalization matters for text input.

# Save System

The game saves:

* Player statistics
* Gold
* Experience
* Level
* Inventory
* Quest progress
* Equipment

You can continue your progress anytime from the main menu.

# Future Improvements

* More enemy types
* Additional quests
* Skills and abilities
* Better AI
* Improved terminal UI
* Sound effects
* More equipment and items

# Developer Notes

This project demonstrates several Object-Oriented Programming concepts, including:

* Classes
* Inheritance
* Polymorphism
* Composition
* Encapsulation
* Game loops
* State management

# Author

Developed by **Ezz Fawzy**

# License

This project is currently not licensed.

# Acknowledgments

Thanks to everyone who provided feedback and suggestions that helped improve this project.
