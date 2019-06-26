# my arsenal

inventory=["sword", "helmet", "shield","armor vest", "heal potion"]
print("my inventory: ")
for item in inventory:
    print(item)
print("in you equ is a:", len(inventory), "items")

# check heal potion in eq

if "heal potion" in inventory:
    print("you will live")

# show selected item in inventory

# index=int(input("tell me index you eq: "))
# print("ok. you selected",inventory[index])

# join 2 list
chest=["gems", "golden coins"]
print ("you find a chest!!! and in it lies:", chest)
print("you got content a chest")
inventory+=chest
print("So! now you eq is:",inventory)

# change sword to mace
print("you changed sword to mace")
inventory[0]="mace"
print("So! and you eq is:",inventory)

# замена двух элементов кортежа, на один

print("You sold a gem and bought a magic crystal for gold coins")

inventory[5:7]=["magic crystal"]

print("You new eq is:",inventory)

# delete item
print("with fight with troll you broken a shield")
del (inventory[2])
print("You new eq is:",inventory)

# del item in list by a slice
print("thiefs steal mace and helmet!!!")
del inventory[:2]
print("You new eq is:",inventory)

