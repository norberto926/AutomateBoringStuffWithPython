def displayinventory(inventory):
    print("Inventory:")
    total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total += count
    print(f"Total number of items: {total}")
             
             
inventory = {'gold coin': 42, 'rope': 1}

displayinventory(inventory)

def addToInventory(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item] += 1
        else:   
            inventory[item] = 1
    
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory, dragonLoot)
        
displayinventory(inventory)