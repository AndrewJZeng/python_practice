stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def inventoryprint(inventory):
    itemtotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemtotal += v
    return itemtotal
print('Inventory:')
items = inventoryprint(stuff)
print('Total Items: ' + str(items))