inventory=()
if not inventory:
    print("you disarmed!")

input("нажми и продолжи")
# наполняем кортеж

inventory=("меч","кольчуга","коктейль молотова","конституция рф")

# выводим наш eq

print("наша экипа: ",inventory)

print("выведем по порядку")
for item in inventory:
    print (item)