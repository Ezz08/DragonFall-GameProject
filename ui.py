from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from pyfiglet import figlet_format
from rich.panel import Panel
from rich.align import Align


console = Console()

def game_title():
      console.print(
        Align.center(
            f"[bold red]{figlet_format('Dragonfall')}[/bold red]"
        )
      )

def main_menu_panel():
    menu = """
[cyan]1.[/cyan] Characters
[cyan]2.[/cyan] Inventory
[cyan]3.[/cyan] Battle Arena
[cyan]4.[/cyan] Quest Board
[cyan]5.[/cyan] Merchant
[cyan]6.[/cyan] Save Game
[cyan]7.[/cyan] Load Game
[cyan]8.[/cyan] Exit
"""

    console.print(
        Align.center(
            Panel(
                menu,
                title="[bold yellow]Main Menu[/bold yellow]",
                border_style="green"
            )
        )
    )


def character_menu_panel():
    menu = """
[cyan]1.[/cyan] Player
[cyan]2.[/cyan] Enemies
[cyan]3.[/cyan] Boss
[cyan]4.[/cyan] Back
"""

    console.print(
        Align.center(
            Panel(
                menu,
                title="[bold yellow]Characters[/bold yellow]",
                border_style="blue"
            )
        )
    )

def inventory_menu_panel():
    menu = """
[cyan]1.[/cyan] Show Inventory
[cyan]2.[/cyan] Search Item
[cyan]3.[/cyan] Remove Item
[cyan]4.[/cyan] Back
"""

    console.print(
        Align.center(
            Panel(
                menu,
                title="[bold yellow]Inventory[/bold yellow]",
                border_style="green"
            )
        )
    )

def battle_menu_panel():
    menu = """
[cyan]1.[/cyan] Fight Goblin
[cyan]2.[/cyan] Fight Skeleton
[cyan]3.[/cyan] Fight Dark Mage
[cyan]4.[/cyan] Fight Dragon
[cyan]5.[/cyan] Back
"""

    console.print(
        Align.center(
            Panel(
                menu,
                title="[bold red]Battle Arena[/bold red]",
                border_style="red"
            )
        )
    )

def quest_menu_panel():
    menu = """
[cyan]1.[/cyan] View Quests
[cyan]2.[/cyan] Claim Rewards
[cyan]3.[/cyan] Back
"""

    console.print(
        Align.center(
            Panel(
                menu,
                title="[bold magenta]Quest Board[/bold magenta]",
                border_style="magenta"
            )
        )
    )

def shop_menu_panel():
    menu = """
[cyan]1.[/cyan] Buy Item
[cyan]2.[/cyan] Back
"""

    console.print(
        Align.center(
            Panel(
                menu,
                title="[bold yellow]Merchant[/bold yellow]",
                border_style="yellow"
            )
        )
    )        
   