# whats integer ? и угадать надо за 5 попыток или проиграл

# количество попыток
count=1

print("\t Отгадай число! за 5 попыток")
print("Попытка 1 (один)!")
import random

# попытки изначально
trires=1
# случайное число
the_number=random.randint(1,100)

# запрашиваем что предложит пользователь
print ("загаданое число:", the_number)
guess=int(input("твое предложение: "))

# пошел перебор
while guess!=the_number:
    
    if count==5:
        print("game over")
        break
        
    count+=1
    print ("попытка: ",count)
            
    if guess>the_number:
        print("меньше!")
    else:
        print("больше")
    guess=int(input("твое предложение: "))
    trires+=1
    
    
if guess==the_number:
    print("Вам удалось угадать число за", trires, "попыток", "и загаданым числом было:", the_number)
else:
    print("не удалось вам за 5 (пять) попыток угадать число -", the_number)