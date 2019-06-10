# whats integer ?

print("\t Отгадай число!")
import random

# попытки изначально
trires=1
# случайное число
the_number=random.randint(1,100)

# запрашиваем что предложит пользователь

guess=int(input("твое предложение: "))

# пошел перебор
while guess!=the_number:
    if guess>the_number:
        print("меньше!")
    else:
        print("больше")
    guess=int(input("твое предложение: "))
    trires+=1

print("Вам удалось угадать число за", trires, "попыток", "и загаданым числом было:", the_number)