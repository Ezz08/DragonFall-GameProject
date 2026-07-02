class Seller:
    def __init__(self, items):
        self.items = items

    def show_items(self, player):

     for item in self.items:

        if player.level >= item.required_level:

            print(
                f"{item.name} | "
                f"Price: {item.price} Gold | "
                f"Required Level: {item.required_level}"
            )
        else:

            print(
                f"{item.name} | "
                f"LOCKED | "
                f"Required Level: {item.required_level}"
            )   


    def buy_item(self, player, item_name):
        for item in self.items:

            if item.name == item_name:

                if player.level < item.required_level:
                  print("Level too low")
                  return
                
                if player.gold < item.price:
                    print("Not enough gold")
                    return
                
                player.spend_gold(item.price)
                player.inventory.add_item(item)

                print(f"{item.name} purchased!")
                return

        print("Item not found")    

    def get_item(self, item_name):

      for item in self.items:

        if item.name == item_name:
            return item

      return None    

