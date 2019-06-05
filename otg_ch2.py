# отгадай число

print("отгадай число за 7 попыток.");

import random;

the_number=int(random.randint(1,100));
tries=1;
print("Попытка №: ",tries);
guess=int(input("Ваше предложение: "));


# цикл отгадывания

while the_number!=guess:
    tries+=1;
    if tries>7:
        print ("Game over! You are loose!");
        break;
    
    if guess>the_number:
        print("Меньше!..");
    else:
        print("Больше!..");
        
    print("Попытка №: ",tries);
    guess=int(input("Ваше предложение: "));
    
if tries<=7:    
    print ("Ура! Вам удалось отгадать число! Это в самом деле:", the_number);    
    print("Вы затратили на это упражнение", tries, "попыток\n");