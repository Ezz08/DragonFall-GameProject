from items import Item
class Inventory:
    def __init__(self):
        self.items = []
        self.items_lookup = {}
    
    def add_item(self, item):
        self.items.append(item)
        self.items_lookup[item.name] = item
    
    def remove_item(self, item):
      if item in self.items:
        self.items.remove(item)
        print(f"🗑️ {item.name} removed from inventory!")      

                   
    def search_item(self, item_name):
        return self.items_lookup.get(item_name, None)

    def has_item(self, name):
        return any(i.name == name for i in self.items)   

    def __str__(self):
     if not self.items:
        return "\n=== INVENTORY ===\nInventory is empty."

     result = "\n=== INVENTORY ===\n"

     for i, item in enumerate(self.items, start=1):
        result += (
            f"{i}. {item.name}\n"
            f"   Price: {item.price}\n"
            f"   Level Required: {item.required_level}\n"
            f"   Description: {item.description}\n\n"
        )

     return result    
        
