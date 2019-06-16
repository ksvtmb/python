inventory=()
if not inventory:
    print("you disarmed!")

input("нажми и продолжи")
# наполняем кортеж

inventory=("меч","кольчуга","коктейль молотова","конституция рф")

# выводим наш eq

print("наша экипа: ",inventory, "и в ней: ",len(inventory),"предметов")

if "коктейль молотова" in inventory:
    print("да вы батюшка! экстремист")
    input("за тобой уже выехали!")

print("выведем по порядку")
for item in inventory:
    print (item)

print("демонстрируем не сильную штуку:", inventory[3])
print("демонстрируем Oldschool:", inventory[:2])

added=("бутылка сэма", "визитка яроша")
inventory+=added
print(inventory)