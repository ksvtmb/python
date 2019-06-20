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

index=int(input("tell me index you eq: "))
print("ok. you selected",inventory[index])

# join 2 list
chest=["gems", "golden coins"]
print ("you find a chest!!! and in it lies:", chest)
print("you got content a chest")
inventory+=chest
print("So! now you eq is:",inventory)
